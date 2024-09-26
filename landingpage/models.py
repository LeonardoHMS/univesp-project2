from django.db import models


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200,
        verbose_name="Nome",
    )
    description = models.TextField(
        max_length=200,
        verbose_name="Descrição",
    )
    bootstrap_icon = models.CharField(
        max_length=200,
        verbose_name="Bootstrap icon",
    )

    def __str__(self):
        return self.name


class ClientContact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200,
        verbose_name="Nome",
    )
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(
        max_length=20,
        verbose_name="Telefone",
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="service",
        verbose_name="Serviço",
    )
    message = models.TextField(
        max_length=300,
        verbose_name="Mensagem",
    )

    def __str__(self):
        return self.name


class HomePageGalleryView(models.Model):
    id = models.AutoField(primary_key=True)
    alt = models.CharField(
        max_length=200,
        verbose_name="Nome Alternativo",
    )
    cover = models.ImageField(
        upload_to="home/covers/%Y/%m/%d",
        blank=True,
        default="",
        verbose_name="Foto",
    )

    def __str__(self):
        return self.name
