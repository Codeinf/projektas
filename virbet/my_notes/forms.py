from django import forms
from tinymce.widgets import TinyMCE
from .models import Note, NoteCategory


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('note_content', 'note_category', 'title', 'user',)
        widgets = {
            'content': TinyMCE(),
            'category': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }