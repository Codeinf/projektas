from django.urls import path
from .views import NoteCreateView


urlpatterns = [
    path('notecreate/', NoteCreateView.as_view(), name='note-create'),
]