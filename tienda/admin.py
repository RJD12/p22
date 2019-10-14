from django.contrib import admin
from .models import Proyecto,Categoria,Image,Integrante

admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(Image)
admin.site.register(Integrante)
# Register your models here.
