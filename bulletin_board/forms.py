from django import forms
from .models import Rubric, Bboard
from users.models import CustomUser


class RubricForm(forms.ModelForm):
    class Meta:
        model = Rubric
        fields = ('name',)


class BboardForm(forms.ModelForm):
    class Meta:
        model = Bboard
        fields = ('title', 'content', 'price', 'rubric')
