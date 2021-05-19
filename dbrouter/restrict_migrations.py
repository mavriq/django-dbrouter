# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import django


class RestrictMigrations(object):
    '''
    Database router that allows you to specify a database to which you can not apply migrations
    Usage:
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        },
        'some_read_only_external_database': {
            'NAME': 'some_read_only_external_database',
            .....
            'allow_migrate': False,
            # False - disable migrations
            # True - do not disable migrations
            # None - default
        },
    }
    DATABASE_ROUTERS = [
        'dbrouter.RestrictMigrations',
        ...
    ]

    ```
    '''

    def db_for_read(self, model, **hints):
        pass

    def db_for_write(self, model, **hints):
        pass

    def allow_relation(self, obj1, obj2, **hints):
        pass

    def allow_migrate(self, db, *args, **kwargs):
        return django.conf.settings.DATABASES[db].get('allow_migrate')
