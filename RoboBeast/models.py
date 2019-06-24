from django.contrib.auth.models import User
from django.db import models
import random

from django.utils.crypto import get_random_string


class Base(models.Model):
    is_active = models.BooleanField(default=True)
    deactivation_reason = models.CharField(max_length=256, blank =True, null=True, default=None)
    created_by = models.CharField(max_length=200, blank=True, null=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_by = models.CharField(max_length=200, blank=True, null=True, default=None)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(Base):
    user_id = models.CharField(max_length=16, blank=True, null=True, default=None, unique=True)
    first_name = models.CharField(null=True, max_length=256, blank=False, default=None, )
    last_name = models.CharField(null=True, max_length=256, blank=False,)
    username = models.CharField(blank=True, max_length=256, unique=True)
    display_Image = models.FileField(upload_to="DisplayImage", blank=True)
    description = models.TextField(max_length=200, default=None)
    city = models.CharField(max_length=100, default=None)
    address = models.TextField(max_length=200)
    phone = models.CharField(max_length=13, unique=True)

    class Meta:
        db_table = 'db_user_profile_table'
        verbose_name = "User Profile"
        verbose_name_plural = "User Profile"

    def save(self, **kwargs):
        b = self.first_name[:2]
        c = self.last_name[:2]
        number = '{:03d}'.format(random.randrange(1, 999))
        self.username = (b + c + number)
        super(UserProfile, self).save(**kwargs)
        if not self.user_id:
            self.user_id = get_random_string(length=6)
        super(UserProfile, self).save(**kwargs)

    def __str__(self):
        return str(self.username)
