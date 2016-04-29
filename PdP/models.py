from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class ColorChoice(models.Model):
    """docstring for ColorChoice"""
    favorite_colors = models.CharField(max_length=128)


class ColorChoiceForm(ModelForm):
    class Meta:
        model  = ColorChoice
        fields = ('favorite_colors',)


class GreenEq(models.Model):
    utilisateur = models.ForeignKey(User)

    def __unicode__(self):
        return "%s" % self.utilisateur


class RedEq(models.Model):
    utilisateur = models.ForeignKey(User)

    def __unicode__(self):
        return "%s" % self.utilisateur


class YellowEq(models.Model):
    utilisateur = models.ForeignKey(User)

    def __unicode__(self):
        return "%s" % self.utilisateur


class BlueEq(models.Model):
    utilisateur = models.ForeignKey(User)

    def __unicode__(self):
        return "%s" % self.utilisateur


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
