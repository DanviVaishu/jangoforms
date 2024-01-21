from django import forms
from app.models import *
from django.core import validators
def validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is less than 5')
def validate_for_a(data):
    if data.startswith('a'):
        raise forms.ValidationError('started with a')
class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validate_for_len,validate_for_a])
    Slocation=forms.CharField(validators=[validators.MinLengthValidator(5)])
    Sprincipal=forms.CharField()
    Email=forms.EmailField()
    ReenterEmail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)
    
    def clean(self):
        e=self.cleaned_data['Email']
        re=self.cleaned_data['ReenterEmail']
        if e!=re:
            raise forms.ValidationError("mismatched")
        

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError("botcatcher")