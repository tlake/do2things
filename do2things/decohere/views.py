from django.views.generic import TemplateView, FormView
from django.shortcuts import render_to_response
from .models import Decoherence
from .forms import DecoherenceForm
from quantumrandom import randint


class HomePageView(TemplateView):
    template_name = 'home.html'


class DecohereView(FormView):
    template_name = 'decohere.html'
    form_class = DecoherenceForm
    success_url = '/decoherence'

    def form_valid(self, form):
        decohered = form.data['state1']

        if randint(0, 2) > 0:
            decohered = form.data['state2']

        decoherence = Decoherence(
            state1=form.data['state1'],
            state2=form.data['state2'],
            decohered=decohered,
        )

        decoherence.save()

        return render_to_response(
            'decoherence.html',
            {'decohered': decohered}
        )


class DecoherenceView(TemplateView):
    template_name = 'decoherence.html'
