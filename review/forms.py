from django import forms

class Review(forms.Form):
    review = forms.CharField(widget=forms.Textarea)