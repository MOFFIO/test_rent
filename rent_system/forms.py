from django import forms
from django.forms import ModelForm

from rent_system.models import Renter, RentUnit
from rent.settings import DATE_INPUT_FORMATS


class RenterForm(ModelForm):

    class Meta:
        model = Renter
        fields = '__all__'


class RentUnitForm(ModelForm):
    start_in = forms.DateField(required=False, input_formats=DATE_INPUT_FORMATS)
    expire_at = forms.DateField(required=False, input_formats=DATE_INPUT_FORMATS)

    class Meta:
        model = RentUnit
        fields = '__all__'

