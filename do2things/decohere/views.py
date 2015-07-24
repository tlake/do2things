from django.views.generic import TemplateView, FormView
from django.shortcuts import render_to_response
from .forms import TwoThingsForm
from quantumrandom import randint


class HomePageView(TemplateView):
    template_name = 'home.html'


class DecohereView(FormView):
    template_name = 'decohere.html'
    form_class = TwoThingsForm
    success_url = '/decohere'

    def form_valid(self, form):
        thing_to_do = form.data['thing_1']

        if randint(0, 2) > 0:
            thing_to_do = form.data['thing_2']

        return render_to_response('dothis.html', {'thing_to_do': thing_to_do})


class DoThisView(TemplateView):
    template_name = 'dothis.html'
