from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class DecohereView(TemplateView):
    template_name = 'decohere.html'
