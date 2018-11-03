'''
Created on 2018/10/24

@author: stomo
'''
from django import forms

class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')
    