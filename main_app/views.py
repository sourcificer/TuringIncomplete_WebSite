from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClientContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home_page(request):

    if request.method == 'GET':
        form = ClientContactForm()
    else:
        form = ClientContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message,email,['tenssyonben@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('home_page')

    return render(request,'index.html',{'form':form})