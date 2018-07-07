from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(label="密码")
    file = forms.FileField(label="头像",required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(label="密码")