from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    email = forms.EmailField(
        label='',  # Establecer la etiqueta como vacía
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
