from django import forms
class TypeSearchForm(forms.Form):
    type_name=forms.CharField(label='Pokemon Name',max_length=100)
