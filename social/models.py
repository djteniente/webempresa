from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name = "Nombre Clave", max_length=(100), unique=True)
    name = models.CharField(verbose_name = "Red Social", max_length=(200))
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(verbose_name="Fecha de Creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de Edición", auto_now=True)

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlacescategorias"
        ordering = ['-name']

    def __str__(self):
        return self.name