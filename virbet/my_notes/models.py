from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )    
    title = models.CharField(max_length=200)
    note_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.title)}, {str(self.created_at)}'

    class Meta:
        ordering = ('created_at',)