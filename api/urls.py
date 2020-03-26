from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import CustomerViewSet, WorkViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('customers', CustomerViewSet)
router.register('works', WorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]