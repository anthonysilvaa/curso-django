from django.db import models
from ordered_model.models import OrderedModel

# Create your models here.


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    descricao = models.TextField()

    class Item(OrderedModel):
        name = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
