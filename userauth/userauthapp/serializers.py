
from django.db.models import fields
from rest_framework import serializers
from .models import User
 
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('cust_id','cust_mobile','cust_username','cust_password','cust_name')

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']