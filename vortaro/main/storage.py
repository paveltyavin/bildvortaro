import os
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.conf import settings
from vortaro.main.git import GIT_REVISION


class VortaroStaticFilesStorage(StaticFilesStorage):
    def post_process(self, paths, dry_run=False, **options):
        if dry_run:
            return []
        has_node = os.system('node -v')
        if has_node != 0:
            return []

        os.chdir(settings.STATIC_ROOT)
        os.system('echo ' + GIT_REVISION + ' > git-revision.txt')

        os.chdir(settings.SRC_ROOT)
        os.system('npm install')
        os.system('node ./node_modules/grunt-cli/bin/grunt --revision={0} --staticdir={1} '.format(
                GIT_REVISION, settings.STATIC_ROOT)
        )
        return []
