import os
from django.contrib.staticfiles.storage import StaticFilesStorage


class VortaroStaticFilesStorage(StaticFilesStorage):
    def post_process(self, paths, dry_run=False, **options):
        if dry_run:
            return []
        has_node = os.system('node -v')
        if has_node != 0:
            return []
