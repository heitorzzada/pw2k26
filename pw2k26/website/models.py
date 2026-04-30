from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return self.nome_cliente
