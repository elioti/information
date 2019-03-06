"""information URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from info.views import UserViewSet, AdminViewSet
from rest_framework_jwt.views import verify_jwt_token, ObtainJSONWebToken
from django.views.generic import TemplateView
from django.conf.urls import static
from information import settings
router = DefaultRouter()
router.register(r'members', UserViewSet, base_name='users')
router.register(r'users', AdminViewSet, base_name='users')

urlpatterns = [
    url(r'login', ObtainJSONWebToken.as_view()),
    url(r'^info$', verify_jwt_token),
    url(r'api/', include(router.urls)),
    url(r'^index', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static'),
]
#urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


