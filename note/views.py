from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import NoteSerializer
from note.models import Note

# Create your views here.

class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            note = self.get_object()
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    