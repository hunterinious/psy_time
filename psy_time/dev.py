from __future__ import absolute_import, unicode_literals

from .settings import *

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console', ],
        },
}
