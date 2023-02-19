from django.db import models




class Home(models.Model):
    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    contact_email = models.EmailField('Email de contacto', blank=True, null=True)
    phone = models.CharField('telefono de contacto', max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_create = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'pagina Principal'
        verbose_name_plural = 'pagina Principal'

        def __str__(self):
            return self.title   
    




        
class Subscribers(models.Model):
    email = models.EmailField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_create = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'suscripctor'
        verbose_name_plural = 'Suscriptores'
        
    
    def __str__(self):
        return self.email
    


class Contact(models.Model):
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    messagge = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_create = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name
