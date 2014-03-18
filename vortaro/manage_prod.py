#!/home/vinograd19/vortaro/env/bin/python

import os
import sys

if __name__ == "__main__":
    sys.path.insert(0, '/home/vinograd19/vortaro/src/')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vortaro.main.settings.prod")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
