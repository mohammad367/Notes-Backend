from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers, models


class NoteViewSet(ModelViewSet):
    serializer_class = serializers.NoteSerializer
    queryset = models.Note.objects.all()
    ordering_fields = ['updated']
# Create your views here.
