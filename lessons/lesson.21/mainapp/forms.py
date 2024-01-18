from django import forms
from .models import Animal, Category, Food

class AnimalForm(forms.ModelForm):

    name = forms.CharField(
        label='Имя',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input animal name',
                'class': 'form-control'
            }
        )
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    food = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'form-control'
            }
        )
        # widget = forms.SelectMultiple(
        #     attrs={
        #         'class': 'form-control'
        #     }
        # )
    )

    class Meta:
        model = Animal
        fields = '__all__'
        # fields = ('name', 'category')
        # exclude = ('category',)


class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))