import datetime

from django import forms
from django.utils import timezone

from mainapp.models import Dog, Food


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        # fields = '__all__'
        fields = ('nickname', 'breed', 'birth_date', 'photo',)
        # exclude = ('birth_date',)

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        current_date = timezone.now().date()
        years_ago_date = current_date - timezone.timedelta(days=36525)

        if birth_date < years_ago_date or birth_date > current_date:
            raise forms.ValidationError(f'Дата рождения не быть позже текущей даты и ниже на 100 лет')

        return birth_date


class FoodForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class ParentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
