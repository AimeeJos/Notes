from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
from notes.models import Notes
from notes.serializers import NotesListSerializer, NotesSerializer

class NotesViews(ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all().order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return NotesListSerializer
        return self.serializer_class
