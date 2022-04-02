from rest_framework.routers import SimpleRouter
from user.viewsets import UserViewSet
from auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from .clinic_history.views import PersonView, CustomerView, TreatmentView, OdontogramView, DentalPieceView

routes = SimpleRouter()

routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

routes.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *routes.urls
]