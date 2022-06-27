from django.db import models
from django.contrib.auth.models import User


class NoteCategory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')
        ordering = ('name', )


class Note(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    note_category = models.ForeignKey(
        NoteCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    note_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.title)}, {str(self.created_at)}'

    class Meta:
        ordering = ('-updated_at', '-created_at',)




