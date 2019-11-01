from django.contrib import admin
from .models import Receta,Categoria,Image,Integrante

admin.site.register(Categoria)
admin.site.register(Receta)
admin.site.register(Image)
admin.site.register(Integrante)
# Register your models here.
