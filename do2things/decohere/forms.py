from django.forms import ModelForm, TextInput
from decohere.models import TwoThings


class TwoThingsForm(ModelForm):
    class Meta:
        model = TwoThings
        fields = ['thing_1', 'thing_2']

        widgets = {
            'thing_1': TextInput(attrs={
                'id': 'thing_1',
                'class': 'twothings',
            }),

            'thing_2': TextInput(attrs={
                'id': 'thing_2',
                'class': 'twothings',
            }),
        }
