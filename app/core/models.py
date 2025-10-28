from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural= 'Tipos'
        db_table = 'tipo'

class Employe(models.Model):
    type   = models.ForeignKey(Type, on_delete=models.CASCADE)
    names  = models.CharField(max_length=150, verbose_name='Nombres')
    address= models.TextField(max_length=500, verbose_name='Dirección')
    email  = models.EmailField(max_length=100, verbose_name='Correo Electrónico')
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Sueldo')
    avatar = models.ImageField(upload_to='avatar', verbose_name='Imagen', null=True, blank=True)
    cv     = models.FileField(upload_to='cvitae', verbose_name='Currículum Vitae', null=True, blank=True)
    created= models.DateTimeField(auto_now=True, verbose_name='Fecha de Creación')
    updated= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Moficación')
    def __str__(self):
        return self.names
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural= 'Empleados'
        db_table = 'empleado'
        ordering = ['id']