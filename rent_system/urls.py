from django.conf.urls import url, include


from rest_framework import routers
from rent_system import views


router = routers.DefaultRouter()

router.register(r'renter', views.RenterViewSet)
router.register(r'rent_units', views.RentUnitViewSet)

urlpatterns = [
    url(r'^$', views.root),
    url(r'^homepage$', views.homepage, name='homepage'),
    url(r'^renter$', views.renter, name='renter'),
    url(r'^rent_units$', views.rent_units, name='rent_units'),
    url(r'^free_rent_units$', views.free_rent_units, name='free_rent_units'),
    url(r'^rest', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

