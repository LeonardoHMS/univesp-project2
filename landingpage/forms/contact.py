from django import forms

from ..models import Service


def get_service_choices():
    choices = [("", "Selecione um serviço")]
    choices += [(service.id, service.name) for service in Service.objects.all()]
    return choices


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="Nome",
        widget=forms.TextInput(attrs={"placeholder": "Insíra seu nome"}),
    )
    email = forms.EmailField(
        max_length=200,
        label="E-mail",
        widget=forms.TextInput(attrs={"placeholder": "Insíra seu E-mail"}),
    )
    phone = forms.CharField(
        max_length=200,
        label="Número",
        widget=forms.TextInput(attrs={"placeholder": "Insíra seu telefone"}),
    )
    service = forms.ChoiceField(
        label="Serviço",
        choices=get_service_choices(),
    )
    message = forms.CharField(widget=forms.Textarea, label="Mensagem")
