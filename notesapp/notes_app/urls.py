from django.urls import path
from .views import CreateNotesView, GetNotesView, GetNoteByIdView, GetNoteByTitle, UpdateNoteView, DeleteNote

urlpatterns = [
    path('createnote', CreateNotesView.as_view(), name='create note'), 
    path('getallnotes', GetNotesView.as_view(), name='get notes'), 
    path('getnotebyid/<str:id>', GetNoteByIdView.as_view(), name='get note by id'),
    path('getnotebytitle/', GetNoteByTitle.as_view(), name='get_note_by_title'),
    path('deletenote/<str:id>', DeleteNote.as_view(), name='delete note'),
    path('updatenote/<str:id>', UpdateNoteView.as_view(), name='update note')
]