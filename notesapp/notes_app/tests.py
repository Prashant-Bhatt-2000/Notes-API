from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Notes
from .serializer import NotesSerializer
from uuid import uuid4

class CreateNotesViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {'title': 'Test Note', 'body': 'Test body'}

    def test_create_note(self):
        response = self.client.post(reverse('create note'), self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_note_invalid_payload(self):
        invalid_payload = {'title': ''}
        response = self.client.post(reverse('create note'), invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetNotesViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Notes.objects.create(title='Note 1', body='body 1')
        Notes.objects.create(title='Note 2', body='body 2')

    def test_get_all_notes(self):
        response = self.client.get(reverse('get notes'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_notes_no_data(self):
        Notes.objects.all().delete()
        response = self.client.get(reverse('get notes'))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetNoteByIdViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note = Notes.objects.create(title='Test Note', body='Test body')

    def test_get_note_by_id(self):
        response = self.client.get(reverse('get note by id', kwargs={'id': self.note.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_by_invalid_id(self):
        invalid_uuid = str(uuid4()) 
        response = self.client.get(reverse('get note by id', kwargs={'id': invalid_uuid}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GetNoteByTitleTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note = Notes.objects.create(title='Test Note', body='Test body')

    def test_get_note_by_title(self):
        response = self.client.get(reverse('get_note_by_title'), {'title': 'Test Note'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_by_invalid_title(self):
        response = self.client.get(reverse('get_note_by_title'), {'title': 'Invalid Title'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class UpdateNoteViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note = Notes.objects.create(title='Test Note', body='Test body')
        self.valid_payload = {'title': 'Updated Title', 'body': 'Updated body'}

    def test_update_note(self):
        response = self.client.put(reverse('update note', kwargs={'id': self.note.id}), self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note_invalid_payload(self):
        invalid_payload = {'title': ''}
        response = self.client.put(reverse('update note', kwargs={'id': self.note.id}), invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteNoteViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.note = Notes.objects.create(title='Test Note', body='Test body')

    def test_delete_note(self):
        response = self.client.delete(reverse('delete note', kwargs={'id': self.note.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note_invalid_id(self):
        invalid_uuid = str(uuid4())  
        response = self.client.delete(reverse('delete note', kwargs={'id': invalid_uuid}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)