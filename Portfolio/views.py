from django.shortcuts import render, redirect
#SendGrid API libraries
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def home_page(request):
    if request.method == 'GET':
        pass
    else:
        print(request.POST)
        subject = request.POST.get('subject')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(message)

        try:
            mail_message = Mail(
                from_email=email,
                to_emails='tIncomplete19@protonmail.com',
                subject=subject,
                html_content="from: " + name + " Message: " + message
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
    return render(request, 'index.html')