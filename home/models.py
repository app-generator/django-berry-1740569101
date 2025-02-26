# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    facebook = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Profile(models.Model):

    #__Profile_FIELDS__
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, null=True, blank=True)

    #__Profile_FIELDS__END

    class Meta:
        verbose_name        = _("Profile")
        verbose_name_plural = _("Profile")



#__MODELS__END
