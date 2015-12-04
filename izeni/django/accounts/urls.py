from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import (RequestPasswordChange, ResetPassword, UserViewSet,
                    ValidateUserView)

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'reset-password/(?P<email>[a-zA-Z0-9-.+@_]+)/$', RequestPasswordChange.as_view(), name='reset-request'),
    url(r'reset/(?P<validation_key>[a-z0-9\-]+)/$', ResetPassword.as_view(), name='reset-password'),
    url(r'validate/(?P<validation_key>[a-z0-9\-]+)/$', ValidateUserView.as_view(), name='user-validation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
