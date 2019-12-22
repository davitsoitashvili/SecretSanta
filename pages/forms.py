from django import forms
from pages.models import LetterModel

class LetterForm(forms.ModelForm):
    letter = forms.CharField(widget=forms.Textarea(attrs={"cols":100,"rows":20}))
    class Meta:
        model = LetterModel
        fields = ['letter']
