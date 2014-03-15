import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vortaro.main.settings.local")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def _application(environ, start_response):
    status = '200 OK'

    output = ''

    output += 'sys.path = {0}\n'.format(sys.path)

    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]

    start_response(status, response_headers)

    return [output]
