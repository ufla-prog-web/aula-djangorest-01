from django.contrib import admin
from django.urls import path, include
from rest_framework import routers             #acrescentei
from core.views import ClienteViewSet          #acrescentei

router = routers.DefaultRouter()               #acrescentei
router.register(r"clientes", ClienteViewSet)   #acrescentei

urlpatterns = [
    path("api/", include(router.urls)),        #acrescentei
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls"))
]