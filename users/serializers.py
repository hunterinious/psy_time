from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import RegularUser, RegularUserProfile
from locations.serializers import CitySerializer

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


class RegularUserForRetrieveProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularUser
        fields = ('email', )


class RegularUserProfileRetrieveSerializer(serializers.ModelSerializer):
    user = RegularUserForRetrieveProfileSerializer()
    city = CitySerializer()

    class Meta:
        model = RegularUserProfile
        fields = '__all__'


class RegularUserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularUserProfile
        fields = '__all__'


class RegularUserForUpdateProfileSerializer(serializers.ModelSerializer):
    profile = RegularUserProfileUpdateSerializer()
    password = serializers.CharField(write_only=True, required=False, style={
        "input_type": "password"})

    class Meta:
        model = RegularUser
        fields = ('email', 'password', 'profile')

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password))

        profile.name = profile_data.get('name', profile.name)
        profile.save()

        instance.save()
        return instance


