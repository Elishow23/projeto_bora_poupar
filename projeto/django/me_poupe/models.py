from django.db import models

# Create your models here.
class Despesa(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"