"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clinic_history.views import PersonView, CustomerView, TreatmentView, OdontogramView, DentalPieceView
from user.viewsets import UserViewSet
from auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

router = routers.DefaultRouter()

router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

router.register(r'user', UserViewSet, basename='user')

router.register(r'persons', PersonView, basename='persons')
router.register(r'customers', CustomerView, basename='customers')
router.register(r'treatments', TreatmentView, basename='treatments')
router.register(r'odontograms', OdontogramView, basename='odontograms')
router.register(r'dentalpieces', DentalPieceView, basename='dentalpieces')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
