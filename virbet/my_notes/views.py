from django.shortcuts import render
from django.views import generic
from . models import Note, NoteCategory
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import NoteForm



class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    success_url = reverse_lazy('notes')
    template_name = 'my_notes/notecreate.html'
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, ('Created'))
        return super().form_valid(form)