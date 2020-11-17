from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import RegularUserProfile
from psychologists.models import PsychologistUserProfile

User = get_user_model()


class RegularUserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularUserProfile
        fields = [
            "name"
        ]


class RegularUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
        "input_type": "password"})
    profile = RegularUserProfileCreateSerializer()

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "profile"
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=User.UserTypes.REGULAR_USER
        )

        profile_data = validated_data.pop('profile')
        RegularUserProfile.objects.create_profile(
            user=user,
            name=profile_data['name']
        )

        return user


class UserLoginDataSerializer(serializers.ModelSerializer):
    profile_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('user_type', 'profile_id', )

    def get_profile_id(self, obj):
        return obj.profile.id
