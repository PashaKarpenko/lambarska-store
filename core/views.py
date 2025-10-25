from shoes.models import Shoe
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bestsellers'] = Shoe.objects.filter(is_bestseller=True)
        context['new_shoes'] = Shoe.objects.filter(is_new_shoes=True)
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(TemplateView):
    template_name = 'core/contact.html'


class SizesView(TemplateView):
    template_name = 'core/sizes.html'

