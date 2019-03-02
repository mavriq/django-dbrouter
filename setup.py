# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

import os
import sys
from setuptools import setup

PKG_NAME = 'dbrouter'
CWD = os.path.dirname(__file__)


sys.path.insert(0, os.path.join(CWD, PKG_NAME))
from version import __version__


def long_description():
    kwargs = ({"encoding": "utf-8"} if sys.version_info[0] > 2 else {})
    return open(os.path.join(CWD, 'README.md'), 'r', **kwargs).read()


def get_requirements():
    return [
        r
        for r in (
            r.strip() for r in open('requirements.txt', 'r').readlines())
        if r and not r.startswith('#')
    ]


setup(
    name='django-dbrouter',
    version=__version__,
    author='mavriq',
    author_email='admin@mavriq.net',
    url='https://github.com/mavriq/django-dbrouter',
    description='Simple and usable database router for django',
    long_description=long_description(),
    license='LGPG',
    packages=[PKG_NAME],
    install_requires=get_requirements(),
    keywords=['django-dbrouter',
              'DATABASE_ROUTERS',
              'database router',
              'Django'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
    ]
)
