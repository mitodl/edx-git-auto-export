"""
AppConfig for git_auto_export app
"""
import os
import logging

from django.apps import AppConfig
from django.conf import settings

log = logging.getLogger(__name__)


class GitAutoExportConfig(AppConfig):
    """
    App config for this app
    """
    name = 'git_auto_export'

    def ready(self):
        """
        Ready handler. Import signals.
        """
        import git_auto_export.signals
        git_repo_export_dir = getattr(settings, 'GIT_REPO_EXPORT_DIR', '/edx/var/edxapp/export_course_repos')
        if not os.path.exists(git_repo_export_dir):
            # for development/docker/vagrant if GIT_REPO_EXPORT_DIR folder does not exist then create it
            log.error("GIT_REPO_EXPORT_DIR is not available in settings, please create it first")
            os.makedirs(git_repo_export_dir, 0o755)
