# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class GeneralInfo(models.Model):

    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
    specification = models.TextField()

    class Meta:
        abstract = True


class Renter(GeneralInfo):

    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class RentUnit(GeneralInfo):

    HOUSE = 'House'
    COMMERCIAL = 'Commercial'
    ATTRIBUTES = (
        (HOUSE, 'House'),
        (COMMERCIAL, 'Commercial')
                )
    name = models.CharField(max_length=100)
    unit_type = models.CharField(max_length=30, choices=ATTRIBUTES)
    renter = models.ForeignKey(Renter)
    rent = models.DecimalField(max_digits=12, decimal_places=2)
    rented = models.BooleanField(default=False)
    adress = models.CharField(max_length=300, blank=True)
    start_in = models.DateField('start in', null=True, blank=True)
    expire_at = models.DateField('expire at', null=True, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '<Renter: %s, Name: %s, Rent: %s, Unit Type: %s, Rented: %s>' % (self.renter, self.name, self.rent, self.unit_type, self.rented)


class Payment(GeneralInfo):

    date = models.DateField()
    rent = models.DecimalField(max_digits=12, decimal_places=2)
    rent_unit = models.ForeignKey(RentUnit, null=True, blank=True)

