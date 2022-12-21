from django.contrib import admin
from django.urls import path, include
from main.views import EventoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('eventoapi/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))

]