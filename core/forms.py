# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, required=False)
    email = forms.EmailField(label='Your Email', required=True)
    subject = forms.CharField(label='Your Subject', max_length=100, required=False)
    message = forms.CharField(label='Your Message', widget=forms.Textarea, required=True)
