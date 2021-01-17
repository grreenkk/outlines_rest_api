from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serialzes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)



class UserProfileSerializer(serializers.ModelSerializer): #The ModelSerializer uses a meta to configure the serializer to
#point to a particular model
    """Serializers a user profile object"""
    class Meta:#This points the serializer to our UserProfile model
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')#This points to fields we want to manage with our serializer
        extra_kwargs = {
            'password': {
                'write_only': True,#This ensures that the user can only produce or update new object but cannot be used to
                #retrieve objects. So when you initiate a get you wont see the password
                'style': {'input_type': 'password'}#This is for the browsable api. This ensures that the inputted password will not be seen, instead stars will show

            }
        }


    def create(self, validated_data):#This overwrites the default create function belonging to the serializer and then uses our
    # own created create_user function located under our UserProfileManager cla ss, used to create new users
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(#The create_user function was created in out UserProfileManager under models.py
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
