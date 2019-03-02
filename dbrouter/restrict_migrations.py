# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
from django.conf import settings


class RestrictMigrations(object):
    '''
    Database router that allows you to prevent migrations on some DB
    Usage:
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        },
        'external': {
            'ENGINE': 'django.db.backends.postgresql',
            .....
            'allow_migrate': False,
            # False - disable migrations
            # True - do not disable migrations
            # None - default
        }
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
        return settings.DATABASES[db].get('allow_migrate', True) and None
