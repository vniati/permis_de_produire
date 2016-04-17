from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GreenEq(models.Model):
    Utilisateur = models.ForeignKey(User)
    def __unicode__(self):
        return "%s" % self.Utilisateur

class RedEq(models.Model):
    Utilisateur = models.ForeignKey(User)
    def __unicode__(self):
        return "%s" % self.Utilisateur

class YellowEq(models.Model):
    Utilisateur = models.ForeignKey(User)
    def __unicode__(self):
        return "%s" % self.Utilisateur

class BlueEq(models.Model):
    Utilisateur = models.ForeignKey(User)
    def __unicode__(self):
        return "%s" % self.Utilisateur
