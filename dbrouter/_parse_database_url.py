# _parse_database_url.py

import sys
if sys.version_info[0] > 2:
    from urllib.parse import urlparse, parse_qs
else:
    from urlparse import urlparse, parse_qs
import re


def parse_database_url(database_url, **kwargs):
    #
    _jdbc_parser = re.compile('^(?:jdbc:)?(?P<uri>.*)$')
    database_url = _jdbc_parser.search(str(database_url))['uri']
    #
    o = urlparse(database_url)
    #
    _result = {'NAME': o.path.lstrip('/')}
    #
    if not o.scheme or o.scheme.lower() in ('sqlite', 'sqlite3'):
        _result = {
            'NAME': o.path,
            'ENGINE': 'django.db.backends.sqlite3',
        }
    #
    elif o.scheme.lower() in ('pg', 'psql', 'postgres', 'postgresql'):
        _result['ENGINE'] = 'django.db.backends.postgresql'
    elif o.scheme.lower() == 'postgis':
        _result['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
    #
    elif o.scheme.lower() == 'mysql':
        _result['ENGINE'] = 'django.db.backends.mysql'
    elif o.scheme.lower() == 'oracle':
        _result['ENGINE'] = 'django.db.backends.oracle'
    else:
        raise ValueError('Unknown schema on %r' % database_url)
    #
    if _result['ENGINE'] != 'django.db.backends.sqlite3':
        _result['HOST'] = o.hostname
        if o.port:
            _result['PORT'] = o.port
        if o.username:
            _result['USER'] = o.username
        if o.password:
            _result['PASSWORD'] = o.password
    #
    _result.update(kwargs)
    if o.query:
        _result.setdefault('OPTIONS', {})
        _result['OPTIONS'].update({
            k: (v[0] if v.__len__() == 1 else v)
            for k, v in parse_qs(o.query).items()})
    #
    return _result
