from django import forms

class EmailForm(forms.Form):
    customer_email = forms.EmailField(label='Customer Email')
