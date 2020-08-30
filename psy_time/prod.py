from __future__ import absolute_import, unicode_literals

from .settings import *

env = os.environ.copy()

import dj_database_url

DEBUG = False

db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
DATABASES['default'].update(db_from_env)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'