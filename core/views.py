from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from form import EmailForm

def sendmail(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, email, ['Marco_Somma@skillsoft.com'])
				return HttpResponseRedirect('/email/ok/')
			except:
				return HttpResponseRedirect('/email/ko/')
		else:
			return HttpResponseRedirect('/email/invalid/')
	else:
		return HttpResponseRedirect('/email/')  

def email(request):
    return render(request, 'email.html')

def ok(request):
    return render(request, 'ok.html')

def ko(request):
    return render(request, 'ko.html')

# def invalid(request):
#     return render(request, 'ko.html')