from django.forms import ModelForm, TextInput
from decohere.models import Decoherence


class DecoherenceForm(ModelForm):
    class Meta:
        model = Decoherence
        fields = ['state1', 'state2']

        widgets = {
            'state1': TextInput(attrs={
                'id': 'state1',
                'class': 'option_text',
                'placeholder': 'one possible state',
            }),

            'state2': TextInput(attrs={
                'id': 'state2',
                'class': 'option_text',
                'placeholder': 'another possible state',
            }),
        }
