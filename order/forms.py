from django import forms
from .validators import *


class OrderForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'placeholder': 'Вася'}),
        error_messages={
            'required': 'Укажите хотя бы 2 буквы',
            'min_length': 'Укажите не менее 2 буквы',
            'max_length': 'Укажите не более 20 букв',
        },
        min_length=2,
        max_length=20,
        validators=[name_check]
    )
    lastname = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'placeholder': 'Уточкин'}),
        error_messages={
            'required': 'Укажите хотя бы 2 буквы',
            'min_length': 'Укажите не менее 2 буквы',
            'max_length': 'Укажите не более 20 букв',
        },
        min_length=2,
        max_length=20,
        validators=[name_check]
    )
    email = forms.EmailField(
        label='e-mail',
        widget=forms.TextInput(attrs={'placeholder': 'postman@gmail.com'}),
        error_messages={
            'required': 'Нужно заполнить',
            'invalid': 'Неверный адрес:'
        },
        validators=[email_check]
    )
    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(attrs={'placeholder': '+79991234567'}),
        error_messages={'required': 'Нужно заполнить'},
        validators=[phone_number_check]
    )
    address = forms.CharField(
        label='Адрес',
        widget=forms.TextInput(attrs={'placeholder': 'С-Пб, Невский пр., д.3'}),
        error_messages={'required': 'Нужно заполнить'}

    )
    months = forms.TypedChoiceField(
        label='Срок поставки',
        required=False,
        choices=(
            ('1 месяца', '1 месяц'),
            ('3 месяцев', '3 месяца'),
            ('6 месяцев', '6 месяцев'),
            ('12 месяцев', '12 месяцев')
        )
    )
    amount = forms.TypedChoiceField(
        label='Количество',
        required=False,
        choices=(
            ('5 литров/месяц', '5 литров/месяц'),
            ('10 литров/месяц', '10 литров/месяц'),
            ('15 литров/месяц', '15 литров/месяц')
        )
    )
