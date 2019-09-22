from django.shortcuts import render, redirect
<<<<<<< HEAD
=======
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClientContactForm
#SendGrid API libraries
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
>>>>>>> upstream/development

def home_page(request):
<<<<<<< HEAD

    return render(request,'index.html')
=======
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
                mail_message = Mail(
                    from_email=email,
                    to_emails='tIncomplete19@protonmail.com',
                    subject=subject,
                    html_content=message
                )
                print(os.environ.get('SENDGRID_API_KEY'))
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(mail_message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                return redirect('home_page')
            except Exception as e:
                print(e.message)
            return redirect('home_page')
    return render(request, 'index.html', {'form': form})
>>>>>>> upstream/development
