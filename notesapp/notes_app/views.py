from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import NotesSerializer
from .models import Notes

class CreateNotesView(APIView):
    def post(self, request):
        note = request.data
        serializer = NotesSerializer(data=note)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Note Created'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Failed to Create Note'}, status=status.HTTP_400_BAD_REQUEST)

class GetNotesView(APIView):
    def get(self, request):
        notes = Notes.objects.all()
        if notes:
            serializer = NotesSerializer(notes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No notes Found'}, status=status.HTTP_404_NOT_FOUND)


class GetNoteByIdView(APIView):
    def get(self, request, id):
        try:
            note = Notes.objects.get(id=id)
            serializer = NotesSerializer(note) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Notes.DoesNotExist:
            return Response({'message': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)



class GetNoteByTitle(APIView): 
    def get(self, request):
        title = request.query_params.get('title', None)
        if title is None:
            return Response({'message': 'Title parameter is missing'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            note = Notes.objects.get(title=title)
            serializer = NotesSerializer(note)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Notes.DoesNotExist:
            return Response({'message': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)



class UpdateNoteView(APIView):
    def put(self, request, id):
        try: 
            note = Notes.objects.get(id=id)
            serializer = NotesSerializer(note, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Note updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        except Notes.DoesNotExist: 
            return Response({'message': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        except: 
            return Response({'message': 'OOps Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class DeleteNote(APIView):
    def delete(self, request, id):
        try:
            note = Notes.objects.get(id=id)
            note.delete()
            return Response({'message': 'Note Deleted'}, status=status.HTTP_200_OK)
        except Notes.DoesNotExist:
            return Response({'message': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)