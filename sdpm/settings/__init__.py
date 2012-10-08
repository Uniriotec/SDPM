# -*- coding: utf-8 -*-
"""
    nome
    ~~~~~~~~~~~~~~

    Here goes the description of this file.

    :copyright: (c) 2012 by arruda.
"""

import sys
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT =os.path.dirname(PROJECT_ROOT)
sys.path.append(SITE_ROOT)

sys.path.append(os.path.join(PROJECT_ROOT,'apps'))
sys.path.append(os.path.join(PROJECT_ROOT,PROJECT_ROOT, 'libs'))

SECRET_KEY = 'qsgco99_(zziss%lie91lfw$34z#)t8rg)ek+_@=eustbt!-xg'

ON_HEROKU = os.environ.has_key('DATABASE_URL')
print "on_heroku"
print ON_HEROKU

from config import *
from installed_apps import *
from logging import *

NO_DEPRECATION_WARNINGS=False
if not ON_HEROKU:
    NO_DEPRECATION_WARNINGS=True
    from env_dev import *
else:
    from env_prod import *

if NO_DEPRECATION_WARNINGS:
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)


