from django.db import models

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200,
        verbose_name="Nome",
    )
    description = models.TextField(
        max_length=200,
        verbose_name="Descrição",
    )


class ClientContact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200,
        verbose_name="Nome",
    )
    email = models.EmailField(
        verbose_name="E-mail"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Telefone",    
    )
    service = models.ForeignKey(
        Services,
        on_delete=models.PROTECT,
        related_name="service",
        verbose_name="Serviço",
    )
