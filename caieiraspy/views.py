from django.shortcuts import render


from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from caieiras.models import Aluno
from caieiras.serializers import AlunoSerializer

from caieiras rest_framework.filter import searchFilter
class CaieirasViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    SearchFilter = ['^nome', '=idade ']
    queryset = Caieiras.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = CaieirasSerializer