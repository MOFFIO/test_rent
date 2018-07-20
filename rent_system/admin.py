# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from rent_system.models import Renter, RentUnit, Payment


admin.site.register(Renter)
admin.site.register(RentUnit)
admin.site.register(Payment)