from .models import UserWallet
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserWalletSerializer(ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserWallet
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data['user']
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        walletuser = UserWallet.objects.update_or_create(
            user=user, wallet=validated_data['wallet'])
        return walletuser
