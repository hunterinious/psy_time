from django.conf import settings
from datetime import datetime


def get_refresh_expire():
    time = datetime.now()
    epoch = datetime.utcfromtimestamp(0)
    expired_time = time + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
    return (expired_time - epoch).total_seconds() * 1000.0
