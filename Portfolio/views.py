from django.shortcuts import render, redirect
from django.views import View
# SendGrid API libraries
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Portfolio(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        subject = request.POST.get('subject')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            mail_message = Mail(
                from_email=email,
                to_emails='tIncomplete19@protonmail.com',
                subject=subject,
                html_content="from: " + name + " Message: " + message
            )
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(mail_message)
            print(response.headers)
            return redirect('home_page')
        except Exception as e:
            print(str(e))

        return render(request, self.template_name)
