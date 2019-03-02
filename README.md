[[_TOC_]]

# Description

Set of simple and usable database routers for django applitaions


## dbrouter.DbByAppRouter

`dbrouter.DbByAppRouter` allows you to specify django-applications or models, that will work with this database.


## dbrouter.RestrictMigrations

`dbrouter.RestrictMigrations` allows you to specify a database to which you can not apply migrations.
For example, with read-only access.

# Example


```python
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
    # 'dbrouter.DbByAppRouter' usage example
    'external': {
        'NAME': 'some_other',
        .....
        'applications': [
            'some_app',                 #  all models on some_app
            'other_app.OnlyThisModel',  #  OnlyThisModel on other_app
        ],
    },
    # 'dbrouter.RestrictMigrations' usage example
    'some_read_only_external_database': {
        'NAME': 'some_read_only_external_database',
        .....
        'allow_migrate': False,
        # False - disable migrations
        # True - do not disable migrations
        # None - default
    },
}

...
DATABASE_ROUTERS = [
    'dbrouter.DbByAppRouter',
    'dbrouter.RestrictMigrations',
    ...
]
```
