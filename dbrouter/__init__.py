# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from .version import __version__, VERSION
from .by_app import DbByAppRouter
from .restrict_migrations import RestrictMigrations


__all__ = ['__version__', 'VERSION', 'DbByAppRouter', 'RestrictMigrations']
