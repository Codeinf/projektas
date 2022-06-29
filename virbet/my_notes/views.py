from django.shortcuts import render, redirect
from django.views import generic
from . models import Note
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib import messages
from .forms import NoteForm
from django.contrib.auth import get_user
from django.db.models import Q


class UserLoginView(LoginView):
    template_name = 'my_notes/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('notes')


class RegisterView(generic.FormView):
    template_name = 'my_notes/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super(RegisterView, self).get(*args, **kwargs)


class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    success_url = reverse_lazy('notes')
    template_name = 'my_notes/notecreate.html'
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, ('Created'))
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    success_url = reverse_lazy('notes')
    template_name = 'my_notes/noteupdate.html'
    form_class = NoteForm


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notes')
    template_name = 'my_notes/notedelete.html'
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class NoteListView(LoginRequiredMixin, generic.ListView):
    model = Note
    paginate_by = 10
    template_name = 'my_notes/notelist.html'
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=get_user(self.request))

        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(note_content__icontains=search)
            )
        return queryset


class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    template_name = 'my_notes/notedetail.html'
    context_object_name = 'note'
