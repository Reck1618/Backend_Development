from django import forms
from .models import Booking, Menu


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
