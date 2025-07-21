from django import forms
from .models import Product
from .stopwords import stopwords


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

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
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену'})
