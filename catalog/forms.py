from django import forms
from .models import Product
from .stopwords import stopwords


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


class ProductForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price', 'is_published')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and any(word in name.lower() for word in stopwords):
            raise forms.ValidationError('Название не может содержать запрещённые слова.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and any(word in description.lower() for word in stopwords):
            raise forms.ValidationError('Описание не может содержать запрещённые слова.')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')
        return price

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if not user or not user.has_perm('catalog.can_unpublish_product'):
            self.fields.pop('is_published', None)
