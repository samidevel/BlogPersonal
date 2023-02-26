from django.db import models

class EntryManager(models.Manager):

    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,   

        ).order_by('-create_date').first()
    
    def entradas_en_home(self):
        #devuelve las ultimas 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,

        ).order_by('-create_date')[:4]
    
    def entradas_recientes(self):
        #devuelve las ultimas 6 entradas en home
        return self.filter(
            public=True,
            

        ).order_by('-create_date')[:6]
    
    def buscar_entrada(self, kword, categoria):
        #buscar entradas por cateegoria o palabra clave

        if len(categoria) >0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,
                public=True
            ).order_by('-create_date')
        else:

            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-create_date')
