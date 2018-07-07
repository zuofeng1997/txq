from django import forms

class reviewWeibo(forms.Form):
    review = forms.CharField(widget=forms.Textarea)
class writeWeibo(forms.Form):
    content = forms.CharField(widget=forms.Textarea)