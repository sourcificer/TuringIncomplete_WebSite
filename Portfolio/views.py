from django.shortcuts import render, redirect, render_to_response
from django.views import View
import json
from urllib.request import urlopen
from django.http import HttpResponse, JsonResponse
# SendGrid API libraries
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_message(request):
    return JsonResponse({
        "done": True
    })


class Portfolio(View):
    template_name = 'index.html'

    def locationChecker(self, request):
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        country = data['country']
        return country

    def get(self, request, *args, **kwargs):
        country = self.locationChecker(request)

        if country == 'IN':
            currency = '₹'
        else:
            currency = '$'

        context = {
            'country': self.locationChecker(request),
            'currency': currency
        }
        return render(request, self.template_name, {'context':context})

    def post(self, request, *args, **kwargs):
        subject = request.POST.get('subject')
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        country = self.locationChecker(request)
        if country == 'IN':
            currency = '₹'
        else:
            currency = '$'

        context = {
            'country': self.locationChecker(request),
            'currency': currency
        }

        response_data = {}
        try:
            mail_message = Mail(
                from_email=email,
                to_emails='tIncomplete19@protonmail.com',
                subject=subject,
                html_content="from: " + name + " Message: " + message
            )
            # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            # response = sg.send(mail_message)
            # print(response.headers)
            response_data['result'] = "SUCCESS!!"
            # return render(json.dumps(response_data),content_type="application/json")
        except Exception as e:
            print(str(e))
            # return render(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

        return render(request, self.template_name,{'context':context})
