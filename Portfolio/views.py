from django.shortcuts import render, redirect, render_to_response
from django.views import View
import json
from urllib.request import urlopen
from django.http import HttpResponse, JsonResponse
# SendGrid API libraries
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class SendMessageAjaxView(View):

    def send_message(self):
        mail_message = Mail(
            from_email=email,
            to_emails='tIncomplete19@protonmail.com',
            subject=subject,
            html_content="from: " + name + " Message: " + message
        )
        sendGrid = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sendGrid.send(mail_message)
        self.response_data['result'] = "SUCCESS!!"

    def post(self, request, *args, **kwargs):
        self.subject = request.POST.get('subject')
        self.name = request.POST.get('name')
        self.email = request.POST.get('email')
        self.message = request.POST.get('message')
        self.response_data = {}

        try:
            self.send_message()
        except ConnectionError as ex:
            jsonResponse = JsonResponse({
                "error": str(ex)
            })
            jsonResponse.status_code = 500
            return jsonResponse

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
        country = self.locationChecker(request)
        if country == 'IN':
            currency = '₹'
        else:
            currency = '$'

        context = {
            'country': self.locationChecker(request),
            'currency': currency
        }

        return render(request, self.template_name, {
            'context': context
        })


class CartView(View):
    template_name = "cart.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
