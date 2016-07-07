from .models import Account
from rest_framework import viewsets
from .serializers import AccountSerializer
from rest_framework import generics


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountList(generics.ListCreateAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
