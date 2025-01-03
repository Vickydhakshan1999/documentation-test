from django_access_point.serializers.crud import CrudSerializer
from django_access_point.serializers.custom_field import CustomFieldSerializer

from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User

from .models import User, UserCustomField


class UserCustomFieldSerializer(CustomFieldSerializer):
    class Meta:
        model = UserCustomField
        fields = CustomFieldSerializer.Meta.fields


class UserSerializer(CrudSerializer):
    # groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)
      
    #   group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), required=False)
 class Meta:
        model = User
        fields = ["name", "email", "phone_no", "password"]
        

from rest_framework import serializers
from .models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['user_id', 'address', 'date_of_birth']  
