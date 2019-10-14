from django.db import models

# Create your models here.

class Integrante(models.Model):
    """Model definition for Integrante."""
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    corrreo= models.CharField(max_length=50)

    class Meta:
        """Meta definition for Integrante."""

        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return u'/tienda/create'
    

class Categoria(models.Model):
    """Model definition for Categoria."""
    #proyecto= models.ForeignKey(Proyecto,default=None,on_delete= models.PROTECT)
    nombre= models.CharField(max_length=50)
    
    class Meta:
        """Meta definition for Categoria."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return u'/tienda/facturas/%d' % self.id 

class Image(models.Model):
    """Model definition for Image."""
    #proyecto= models.ForeignKey(Proyecto,default=None,on_delete= models.PROTECT)
    imagen= models.ImageField(upload_to="ropa",default=None,null=False)
    class Meta:
        """Meta definition for Image."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.imagen)
    
    def get_absolute_url(self):
        return u'/tienda/create'
    


class Proyecto(models.Model):
    """Model definition for proyecto."""
   
    nombre= models.CharField(max_length=50)
    descripcion= models.TextField(blank=True)
    fecha= models.DateField()
    imagen= models.ImageField(upload_to="ropa",null=False)
    categoria=models.ForeignKey(Categoria,default=None,on_delete= models.PROTECT)
    imagenes=models.ManyToManyField(Image)
    integrantes=models.ManyToManyField(Integrante)
    class Meta:
        """Meta definition for proyecto."""

        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return u'/tienda/%d' % self.id 