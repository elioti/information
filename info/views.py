from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User
from django_filters import rest_framework
from rest_framework import filters
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('id',)
