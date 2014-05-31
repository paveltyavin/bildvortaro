import subprocess
import os
from django.conf import settings


def git_revision():
    try:
        head = subprocess.Popen("git rev-parse HEAD", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, err = head.communicate()
        if out[:5] == 'fatal':
            raise Exception
        return out.strip()
    except:
        try:
            f = open(os.path.join(settings.STATIC_ROOT, 'git-revision.txt'))
            res = f.read()
            f.close()
            return res
        except:
            return u'unknown'

# Calculate revision once at compile time
GIT_REVISION = git_revision()
