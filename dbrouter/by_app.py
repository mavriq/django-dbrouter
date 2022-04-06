# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import sys
import django
try:
    from django.utils.six import string_types
except ImportError:
    if sys.version_info[0] > 2:
        string_types = (str, )
    else:
        from six import string_types


class DbByAppRouter(object):
    '''
    Database router, that allows you to specify django-applications or models, that will work with this database.

    Usage:
    ```
    INSTALLED_APPS = [
        ...
        'some_app',
        'other_app',
    ]
    ...
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        },
        'external': {
            'ENGINE': 'django.db.backends.postgresql',
            .....
            'applications': [
                'some_app',                 #  all models on some_app
                'other_app.OnlyThisModel',  #  OnlyThisModel on other_app
            ]
        }
    }
    DATABASE_ROUTERS = [
        'dbrouter.DbByAppRouter',
        ...
    ]
    ```
    '''

    DEFAULT = 'default'

    def __init__(self):
        self.app_databases = {}
        for db, opts in django.conf.settings.DATABASES.items():
            apps = opts.get('applications')
            if not apps:
                continue
            elif isinstance(apps, string_types):
                self.app_databases[apps] = db
            elif hasattr(apps, '__iter__'):
                for app in apps:
                    self.app_databases[app] = db
            else:
                raise AttributeError(
                    '`applications` must be string or list of strings')

    def __get_database_of_names(self, app_label, model_name):
        return (self.app_databases.get('{0}.{1}'.format(app_label, model_name))
                or
                self.app_databases.get(app_label, self.DEFAULT))

    def _get_database_of(self, model):
        app_label = model._meta.app_label
        model_name = model.__name__
        return self.__get_database_of_names(app_label, model_name)

    def db_for_read(self, model, **hints):
        return self._get_database_of(model)

    def db_for_write(self, model, **hints):
        return self._get_database_of(model)

    def allow_relation(self, obj1, obj2, **hints):
        return (self._get_database_of(obj1.__class__) ==
                self._get_database_of(obj2.__class__)) and None

    if django.VERSION > (1, 8):
        def allow_migrate(self, db, app_label, model_name=None, **hints):
            model = hints.get('model', None)
            if model:
                return (db == self._get_database_of(model)) and None
            else:
                return (db == self.__get_database_of_names(
                    app_label, model_name)) and None
    else:
        def allow_migrate(self, db, model):
            return (db == self._get_database_of(model)) and None
