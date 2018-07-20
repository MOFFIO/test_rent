from rent_system.models import Renter, RentUnit
from rest_framework import serializers


class RenterSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Renter
                fields = '__all__'

class RentUnitSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = RentUnit
                fields = '__all__'