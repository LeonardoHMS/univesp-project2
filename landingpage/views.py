from django.views.generic import TemplateView

from .forms.contact import ContactForm
from .models import HomePageGalleryView, Service


class HomeView(TemplateView):
    template_name = "global/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["services"] = Service.objects.all()
        context["galleryviews"] = HomePageGalleryView.objects.all()
        context["clientcontact"] = ContactForm()

        return context
