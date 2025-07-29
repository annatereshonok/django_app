from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': field.label or name.capitalize()
                })


class CustomUserCreationForm(FormControlMixin, UserCreationForm):
    phone = forms.CharField(required=False, label='Телефон')
    country = forms.CharField(required=False, label='Страна проживания')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'phone', 'country', )

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone


class CustomAuthenticationForm(FormControlMixin, AuthenticationForm):
    model = CustomUser
    fields = ('email', )

