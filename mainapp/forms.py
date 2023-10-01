import datetime

from django import forms

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
        fields = ('nickname', 'breed', 'birth_date', 'photo', 'email',)
        # exclude = ('birth_date',)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if 'sky.pro' not in cleaned_data:
            raise forms.ValidationError('Почта должна относиться к учебному заведению')

        return cleaned_data


class FoodForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class ParentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
