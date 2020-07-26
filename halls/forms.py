from django import forms
from django.forms import formset_factory

class SearchVideoForm(forms.Form):
    search_term = forms.CharField(max_length=255,label = 'Search for videos')