from django.db import models
from datetime import datetime


class Ordflokkur(models.Model):
    ordflokkur = models.CharField(max_length=255, blank=True, null=True)
    jp_heiti = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ordflokkur


class Efnisflokkur(models.Model):
    efnisflokkur = models.CharField(max_length=255, blank=True, null=True)
    jp_heiti = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.efnisflokkur


class Malsnid(models.Model):
    malsnid = models.CharField(max_length=255, blank=True, null=True)
    jp_heiti = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.malsnid


class JpJafnheiti(models.Model):
    jp_jafnheiti = models.CharField(max_length=255)
    ath = models.CharField(max_length=700, blank=True, null=True)
    mynd = models.ImageField(upload_to='fletta_images', blank=True, null=True)
    uppflettiord = models.ForeignKey('Fletta', models.DO_NOTHING)

    def __str__(self):
        return self.jp_jafnheiti


class Daemi(models.Model):
    daemi = models.CharField(max_length=255, blank=True, null=True)
    jp_thyg = models.CharField(max_length=700, blank=True, null=True)
    uppflettiord = models.ForeignKey('Fletta', models.DO_NOTHING)
    jp_jafnheiti = models.ForeignKey('JpJafnheiti', models.DO_NOTHING)

    def __str__(self):
        return self.daemi


class Ordastaeda(models.Model):
    ordastaeda = models.CharField(max_length=255, blank=True, null=True)
    jp_thyd = models.CharField(max_length=255, blank=True, null=True)
    efnisflokkur = models.ForeignKey('Efnisflokkur', models.DO_NOTHING, blank=True, null=True)
    malsnid = models.ForeignKey('Malsnid', models.DO_NOTHING, blank=True, null=True)
    mynd = models.ImageField(upload_to='fletta_images', blank=True, null=True)
    uppflettiord = models.ForeignKey('Fletta', models.DO_NOTHING)

    def __str__(self):
        return self.ordastaeda


class DaemiOrdastaeda(models.Model):
    daemi_ordastaeda = models.CharField(max_length=255, blank=True, null=True)
    jp_thyd = models.CharField(max_length=700, blank=True, null=True)
    uppflettiord = models.ForeignKey('Fletta', models.DO_NOTHING)
    ordastaeda = models.ForeignKey('Ordastaeda', models.DO_NOTHING)

    def __str__(self):
        return self.daemi_ordastaeda


class Fletta(models.Model):
    uppflettiord = models.CharField(max_length=255)
    ordflokkur = models.ForeignKey('Ordflokkur', models.DO_NOTHING)
    beygingarmynd = models.CharField(max_length=255, blank=True, null=True)
    bin_id = models.IntegerField(blank=True, null=True)
    upptaka = models.FileField(upload_to='fletta_sounds', blank=True, null=True)
    ipa = models.CharField(max_length=255, blank=True, null=True)
    ordmynd = models.CharField(max_length=255, blank=True, null=True)
    efnisflokkur = models.ForeignKey('Efnisflokkur', models.DO_NOTHING, blank=True, null=True)
    malsnid = models.ForeignKey('Malsnid', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    buin = models.BooleanField(default=False)

    def __str__(self):
        return self.uppflettiord
