from django.db import models
from applications.entrada.models import Entry
from django.conf import settings

from .managers import FavoritesManager


class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_favorites', on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='entry_favirutes', on_delete=models.CASCADE)
    create_date   = models.DateTimeField(auto_now_add=True)
    update_create = models.DateField(auto_now=True)

    objects = FavoritesManager()

    class Meta:
        unique_together = ('user', 'entry')
        verbose_name = 'Entrada favorita'
        verbose_name_plural = 'Entradas favoritas'

        
    

