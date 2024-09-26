from django import forms

from ..models import ClientContact, Service


def get_service_choices():
    choices = [("", "Selecione um serviço")]
    choices += [(service.id, service.name) for service in Service.objects.all()]
    return choices


class ContactForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        label="Serviço",
        queryset=Service.objects.all(),
        empty_label="Selecione um serviço",
    )

    class Meta:
        model = ClientContact
        fields = "name", "email", "phone", "service", "message"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Insíra seu nome",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Insíra seu e-mail",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Insíra seu telefone",
                }
            ),
            "message": forms.Textarea(),
        }
