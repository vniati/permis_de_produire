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

class DysStandard(models.Model):
    dysfonctionnement = models.CharField(max_length=128)
    imageVerso = models.CharField(max_length=128)
    description = models.TextField(max_length=1400, default='SOME STRING')
    nom = models.CharField(max_length=20)
    def __unicode__(self):
        return "%s" % self.nom

class DysCritique(models.Model):
    dysfonctionnement = models.CharField(max_length=128)
    imageVerso = models.CharField(max_length=128)
    description = models.TextField(max_length=1400, default='SOME STRING')
    nom = models.CharField(max_length=20)
    def __unicode__(self):
        return "%s" % self.nom

class Rattrapage(models.Model):
    categorie = models.CharField(max_length=128)
    dysfonctionnement = models.CharField(max_length=128)
    imageVerso = models.CharField(max_length=128)
    nom = models.CharField(max_length=20)
    def __unicode__(self):
        return "%s" % self.nom
