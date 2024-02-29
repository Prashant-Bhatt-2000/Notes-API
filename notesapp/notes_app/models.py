
from django.db import models
from uuid import uuid4

class Notes(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

