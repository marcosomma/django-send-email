from django import forms

class EmailForm(forms.Form):
	email = forms.EmailField()
	subject = forms.CharField(max_length=255)
	message = forms.CharField()