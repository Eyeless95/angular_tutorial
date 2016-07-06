from .models import Account, Transactions
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Account.objects.create(**validated_data)

    class Meta:
        model = Account
        fields = ('pk', 'name', 'credit_card', 'balance')
