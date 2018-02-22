"""
WSGI config for wheelso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os


from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wheelso.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from configurations.wsgi import get_wsgi_application  # noqa

application = get_wsgi_application()
application = WhiteNoise(application, root='../static')
# application.add_files('/path/to/more/static/files', prefix='more-files/')
