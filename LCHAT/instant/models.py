from django.db import models
from django.conf import settings


class LoggedInUser(models.Model):
    """
    Model to track logged in users
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='logged_in_user')
