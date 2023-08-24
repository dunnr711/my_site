import os

if os.environ.get('ENVIRONMENT') == 'production':
    from .settings_prod import *
else:
    from .settings_dev import *
