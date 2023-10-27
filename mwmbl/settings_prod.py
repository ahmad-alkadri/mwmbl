import os

import dj_database_url

from mwmbl.settings_common import *


SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]


DATABASES = {'default': dj_database_url.config(default=os.environ["DATABASE_URL"])}

DEBUG = True    # TODO set back to False
ALLOWED_HOSTS = ["api.mwmbl.org", "mwmbl.org", "beta.mwmbl.org"]
CSRF_TRUSTED_ORIGINS = list(ALLOWED_HOSTS)


DATA_PATH = "/app/storage"
RUN_BACKGROUND_PROCESSES = False
NUM_PAGES = 10240000
