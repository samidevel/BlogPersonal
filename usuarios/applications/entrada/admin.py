from django.contrib import admin
from .models import Category, Entry, Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(Tag)
