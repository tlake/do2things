from django.views.generic import TemplateView, FormView
from .forms import TwoThingsForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class DecohereView(FormView):
    template_name = 'decohere.html'
    form_class = TwoThingsForm
    success_url = '/decohere'
