#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: June
# @Time : 2019/3/4
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "datetime": {'read_only': True}
        }

    # def save(self, **kwargs):
    #     """
    #     Save and return a list of object instances.
    #     """
    #     # Guard against incorrect use of `serializer.save(commit=False)`
    #     assert 'commit' not in kwargs, (
    #         "'commit' is not a valid keyword argument to the 'save()' method. "
    #         "If you need to access data before committing to the database then "
    #         "inspect 'serializer.validated_data' instead. "
    #         "You can also pass additional keyword arguments to 'save()' if you "
    #         "need to set extra attributes on the saved model instance. "
    #         "For example: 'serializer.save(owner=request.user)'.'"
    #     )
    #     if len(self.validated_data) == 1:
    #         return super(UserSerializer, self).save(**kwargs)
    #     validated_data = [
    #         dict(list(attrs.items()) + list(kwargs.items()))
    #         for attrs in self.validated_data
    #     ]
    #     old_objs = []
    #     new_objs = []
    #     for item in validated_data:
    #         instance, flag = User.objects.get_or_create(account=item["account"], defaults=item)
    #         if not flag:
    #             old_objs.append(instance)
    #             new_objs.append(item)
    #     print([i.account for i in old_objs])
    #     print([j["account"] for j in new_objs])
    #     # return self.instance


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "is_superuser", "last_login", "password")
        extra_kwargs = {
            "password": {'write_only': True}
        }
