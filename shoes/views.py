from .models import Shoe
from django.views.generic import ListView, DetailView


class ShoesListView(ListView):
    paginate_by = 3
    model = Shoe
    template_name = 'shoes/shoes_list.html'


class ShoeDetailView(DetailView):
    model = Shoe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shoe = self.object
        if shoe.size_from and shoe.size_to:
            context['size_range'] = range(shoe.size_from, shoe.size_to + 1)
        else:
            context['size_range'] = []
        return context

