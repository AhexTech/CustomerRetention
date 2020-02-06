# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Fruithut(models.Model):
    ticket = models.TextField(db_column='TICKET', blank=True, null=False,primary_key=True)  # Field name made lowercase.
    units = models.FloatField(db_column='UNITS', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    reference = models.IntegerField(db_column='REFERENCE', blank=True, null=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
    pricebuy = models.FloatField(db_column='PRICEBUY', blank=True, null=True)  # Field name made lowercase.
    pricesell = models.FloatField(db_column='PRICESELL', blank=True, null=True)  # Field name made lowercase.
    datenew = models.TextField(db_column='DATENEW', blank=True, null=True)  # Field name made lowercase.
    payment = models.TextField(db_column='PAYMENT', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    transid = models.TextField(db_column='TRANSID', blank=True, null=True)  # Field name made lowercase.
    catergory = models.TextField(db_column='CATERGORY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fruithut'

    def __str__(self):
        context={
            'pricesell':self.pricesell,
            'category':self.catergory,
            'units':self.units
        }

        return context