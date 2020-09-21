from django import forms
from .models import Address
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address

        fields = [
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'country',
            'zip_code',
            'phone_number'
        ]
        widgets = {
            'address_line_1': forms.TextInput(attrs={'class':'form-control',
                                    'placeholder': 'address line 1'}),
            'address_line_2': forms.TextInput(attrs={'class':'form-control',
                                    'placeholder': 'address line 2'}),
            'city': forms.TextInput(attrs={'class':'form-control',
                                    'placeholder': 'city'}),
            'state': forms.TextInput(attrs={'class':'form-control',
                                    'placeholder': 'state'}),
            'country': forms.TextInput(attrs={'class':'form-control',
                                    'placeholder': 'country'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control',
                                    'placeholder': 'zip code'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control',
                                    'placeholder': 'phone number'}),

                }
