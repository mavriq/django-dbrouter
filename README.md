# Description

Set of simple and usable database routers for django applitaions


## DbByAppRouter

Database router, позволяющий указать django-приложения и модели, работающие с данной db

## Example


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
    'external': {
        'ENGINE': 'django.db.backends.postgresql',
        .....
        'applications': [
            'some_app',                 #  all models on some_app
            'other_app.OnlyThisModel',  #  OnlyThisModel on other_app
        ],

        'allow_migrate': False,
        # False - disable migrations
        # True - do not disable migrations
        # None - default
    }
}

...
DATABASE_ROUTERS = [
    'dbrouter.DbByAppRouter',
    'dbrouter.RestrictMigrations',
    ...
]
```
