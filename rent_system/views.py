# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets

from rent_system.models import Renter, RentUnit, Payment
from rent_system.forms import RenterForm, RentUnitForm
from rent_system.serializers import RenterSerializer, RentUnitSerializer



def root(request):
    return HttpResponseRedirect('/homepage')


def homepage(request):
    return render(request, 'homepage.html', {
        'rent_units': RentUnit.objects.all()
    })


def renter(request, *args, **kwargs):

    if request.method == 'GET':
        form = RenterForm()
    elif request.method == 'POST':
        form = RenterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('homepage')
    return render(request, 'renter.html', {
        'renter': Renter.objects.all(),
        'form': form
    })


def rent_units(request, *args, **kwargs):
    if request.method == 'GET':
        form = RentUnitForm()
    elif request.method == 'POST':
        form = RentUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('rent_units')

    return render(request, 'rent_units.html', {
        'rent_units': RentUnit.objects.all(),
        'form': form,

    })


def free_rent_units(request, *args, **kwargs):
    context = RentUnit.objects.filter(rented=False)
    return render(request, 'free_rent_units.html', {
    'rent_units': context
    })


class RenterViewSet(viewsets.ModelViewSet):

    queryset = Renter.objects.all()
    serializer_class = RenterSerializer


class RentUnitViewSet(viewsets.ModelViewSet):

    queryset = RentUnit.objects.all()
    serializer_class = RentUnitSerializer
