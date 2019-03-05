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

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "is_superuser", "last_login", "password")
        extra_kwargs = {
            "password": {'write_only': True}
        }
