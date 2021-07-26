from django import forms
from .models import Rubric, Bboard



class RubricForm(forms.ModelForm):
    class Meta:
        model = Rubric
        fields = ('name',)


class BboardForm(forms.ModelForm):
    class Meta:
        model = Bboard
        fields = ('title', 'content', 'price', 'rubric')
