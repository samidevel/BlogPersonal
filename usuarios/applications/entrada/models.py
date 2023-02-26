from datetime import timedelta, datetime

from django.db import models
from django.conf import settings

from django.template.defaultfilters import slugify

#from ckeditor_uploader.fields import RichTextFieldRichTextUploadingField
from ckeditor.fields import RichTextField


# models managers portada
from .manager import EntryManager

            
class Category(models.Model):
    
    short_name=models.CharField('Nombre corto', max_length=15, unique=True)
    name=models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
        

class Tag(models.Model):
    name=models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Entry(models.Model):
    user          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag           = models.ManyToManyField(Tag)
    title         = models.CharField('Titulo', max_length=200)
    resume        = models.TextField() 
   #content = models.RichTextUploadingField('contenido')
    content       = RichTextField(blank=True, null= True)
    public        = models.BooleanField(default=False)
    image         = models.ImageField('Imagen', upload_to='Entry')
    portada       = models.BooleanField(default=False)
    in_home       = models.BooleanField(default=False)
    slug          = models.SlugField(editable=False , max_length=300)
    create_date   = models.DateTimeField(auto_now_add=True)
    update_create = models.DateField(auto_now=True)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.title



    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds =  int(total_time.total_seconds())
        sluge_unique = '%s %s' % (self.title, str(seconds))
        self.slug = slugify(sluge_unique)
        super(Entry, self).save(*args, **kwargs)