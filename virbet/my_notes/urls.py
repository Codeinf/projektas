from django.urls import path
from .views import NoteCreateView, NoteListView, NoteDetailView, NoteUpdateView, NoteDeleteView, UserLoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', NoteListView.as_view(), name='notes'),
    path('notecreate/', NoteCreateView.as_view(), name='note-create'),
    path('notes/', NoteListView.as_view(), name='notes'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note'),
    path('noteupdate/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('notedelete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]