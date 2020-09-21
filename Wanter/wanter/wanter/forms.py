from django import forms
from django.contrib.auth import get_user_model
from django.core import validators
User = get_user_model()

class ContactForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control my-1",
               "placeholder":"Your full name",
                "id":"form_full_name"
               }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control my-1",
               "placeholder":"Your Email",
                "id":"form_full_name"
               }))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control my-1",
           "placeholder":"Your content"
            }))
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email has to be gmail.com or outlook.com")
    #     return email
