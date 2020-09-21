from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()
# class UserAdminCreationForm(forms.ModelForm):
class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class":"col-12 form-control",
                "placeholder":"password"}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={"class":"mt-1 form-control",
                "confirm placeholder":"password"}))

    class Meta:
        model = User
        fields = ('email','full_name','user_image')#'full_name',)
        widgets = {'user_image':forms.FileInput(
        attrs={'style':'display: block;'}),
            'email': forms.TextInput(attrs={'class':'form-control',
                                            'placeholder': 'Email Address'}),
            'full_name': forms.TextInput(
                attrs={'class':'form-control mb-2',
                       'placeholder': 'Full Name'}),
        }
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.active = False # send a confirmation email
        if commit:
            user.save()
        return user



class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name','email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class LoginForm(forms.Form):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(
        attrs={"class":"form-control",
               "placeholder":"Your username",
                "id":"Username"
               }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
           "placeholder":"password"}))

class GuestForm(forms.Form):
    email= forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control",
               "placeholder":"Your Email",
                  }))
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email




# class RegisterForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={"class":"form-control",
#                "placeholder":"username",
#                 "id":"Username"
#                }))
#     email = forms.EmailField(widget=forms.EmailInput(
#         attrs={"class":"form-control",
#                "placeholder":"Your Email",
#                                }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
#            "placeholder":"password"}))
#
#     password2 = forms.CharField(label= 'Confirm password',widget=forms.PasswordInput(attrs={"class":"form-control",
#            "placeholder":"password"}))
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username=username)
#         if qs.exists():
#             raise forms.ValidationError("Username is taken")
#         return username
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("email is taken")
#         return email
#
#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password2 != password:
#             raise forms.ValidationError("Passwords must match.")
#         return data
