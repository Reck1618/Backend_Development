from django import forms
from .models import EntryForm

class EntryForm(forms.ModelForm):
    class Meta:
        model = EntryForm
        fields = '__all__'
