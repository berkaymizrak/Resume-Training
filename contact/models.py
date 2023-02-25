from django.db import models
from core.models import AbstractModel

# Create your models here.

class Message(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    email = models.EmailField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Email',
        help_text='',
    )
    subject = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Subject',
        help_text='',
    )
    message = models.TextField(
        default='',
        blank=True,
        verbose_name='Message',
        help_text='',
    )

    def __str__(self):
        return f'Message: {self.name}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('name',)
