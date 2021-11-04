from django import forms
class Url(forms.Form):
    url = forms.URLField(label="URL")
