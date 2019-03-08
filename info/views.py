from django.shortcuts import render
from .serializers import UserSerializer, AdminSerializer
from rest_framework import viewsets
from .models import User, SiteAdmin
from django_filters import rest_framework
from rest_framework import filters
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
import datetime
from django.utils.timezone import now
from rest_framework.permissions import IsAuthenticated
from utils.permission import IsSuperUser
from django.contrib.auth.hashers import make_password
from django.db.models import Min
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.values('account').annotate(name=Min('name'), id=Min('id'), phone=Min('phone'), qq=Min('qq'), email=Min('email'), wechat=Min('wechat'), datetime=Min('datetime'))
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('id',)
    filterset_fields = ("account", "name", "phone", "qq", "email", "wechat")

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

    def update(self, request, *args, **kwargs):
        if self.lookup_field in self.kwargs and self.kwargs[self.lookup_field] == 'excel':
            accounts = []
            for querry_param in self.request.data:
                account = querry_param.get('account', '')
                if account:
                    accounts.append(account)
            print(accounts)
            users = User.objects.filter(account__in=accounts)
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        else:
            return super(UserViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if self.kwargs[self.lookup_field] == 'all':
            User.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return super(UserViewSet, self).destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        nowtime = now()
        if isinstance(serializer.validated_data, list):
            validated_data = [
                dict(list(attrs.items()) + [('datetime', nowtime)])
                for attrs in serializer.validated_data
            ]
            User.objects.bulk_create([User(**item) for item in validated_data])
        else:
            serializer.save(datetime=nowtime)
        # old_objs = []
        # new_objs = []
        # for item in validated_data:
        #     instance, flag = User.objects.get_or_create(account=item["account"], defaults=item)
        #     if not flag:
        #         old_objs.append(instance)
        #         new_objs.append(item)
        # print([i.account for i in old_objs])
        # print([j["account"] for j in new_objs])


class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser,)
    serializer_class = AdminSerializer
    queryset = SiteAdmin.objects.all().order_by('id')
    filter_backends = (rest_framework.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('id',)

    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data['password']), is_staff=True)
