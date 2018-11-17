from rest_framework import serializers
from account.models import User, OrdinaryUser, Doctor, Symptom, Data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

class DoctorSerializer(serializers.ModelSerializer):
    user=UserSerializer(required=True)
    class Meta:
        model=Doctor
        fields = ('user','yearsOfExperience', 'fieldOfStudy', 'hospital',)
        #read_only_fields=['is_staff','is_doctor','is_superuser','is_active','is_ordinary_user']

    def create(self, validated_data):
        user_data=validated_data.pop('user')
        user=UserSerializer.create(UserSerializer(),validated_data=user_data)
        user.set_password(user.password)
        user.is_doctor = True
        user.save()
        doctor=Doctor.objects.create(user=user,
                                         yearsOfExperience=validated_data.pop('yearsOfExperience'),
                                         fieldOfStudy=validated_data.pop('fieldOfStudy'),
                                         hospital=validated_data.pop('hospital'))
        return doctor

class OrdinaryUserSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=OrdinaryUser
        fields = ['phoneNumber','user',]
    def create(self, validated_data):
        user_data=validated_data.pop('user')
        user=UserSerializer.create(UserSerializer(),validated_data=user_data)
        user.is_ordinary_user = True
        user.set_password(user.password)
        user.save()

        ordinary_user=OrdinaryUser.objects.create(user=user,phoneNumber=validated_data.pop('phoneNumber'))

        return ordinary_user

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields = '__all__'

        def create(self,validated_data):
            data=Data.objects.create(**validated_data)

            return data

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Symptom
        fields=('symptomName',)
