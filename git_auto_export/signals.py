import logging
from django.dispatch import receiver
from xmodule.modulestore.django import SignalHandler

from django.conf import settings
from .tasks import async_export_to_git

log = logging.getLogger(__name__)


@receiver(SignalHandler.course_published)
def listen_for_course_publish(sender, course_key, **kwargs):  # pylint: disable=unused-argument
    """
    Receives publishing signal and performs publishing related workflows
    """
    if settings.FEATURES.get('ENABLE_EXPORT_GIT') and settings.FEATURES.get('ENABLE_GIT_AUTO_EXPORT'):
        # If the Git auto-export is enabled, push the course changes to Git
        log.info(
            'Course published with auto-export enabled. Starting export... (course id: %s)', course_key
        )
        async_export_to_git.delay(str(course_key))
