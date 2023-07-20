from .models import New
from .serializers import *
from rest_framework import viewsets


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
