# sentiment_analysis_app/forms.py
from django import forms

class AnalyzedTextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
