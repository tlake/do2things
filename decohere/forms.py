from django.forms import ModelForm
from decohere.models import TwoThings


class TwoThingsForm(ModelForm):
    class Meta:
        model = TwoThings
        fields = ['thing_1', 'thing_2']
