from django import forms
from delivery.models import DeliveryModel

class DeliveryForm(forms.ModelForm):
    class Meta:
        model=DeliveryModel
        fields='__all__'
    