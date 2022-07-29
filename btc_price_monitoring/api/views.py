import requests

from django.http import JsonResponse

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.views.decorators.csrf import csrf_exempt


def show_paths(request):
    return JsonResponse({'tags': {
        'rate': 'Get the current rate of BTC to UAH',
        'subscription': 'subscribe to newsletter'
    }
    })


def current_rate(request):
    api_btc_url = 'https://api.coingecko.com/api/v3/coins/bitcoin?localization=en'
    response = requests.request('GET', api_btc_url).json()
    if response.get("error"):
        return JsonResponse({'responses': '400',
                             'description': 'Invalid status value'})
    return JsonResponse({'responses': '200',
                         'description': response['market_data']['current_price']['uah']
                         })


@csrf_exempt
def add_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        with open('emails.txt', 'r+') as emails:
            for e in emails.readlines():
                if e.rstrip() == email:
                    return JsonResponse({'responses': '409',
                                         'description': 'This email already in use'})
            emails.write(f'{email}\n')
            return JsonResponse({'responses': '200',
                                 'description': 'Email added successfully'
                                 })


@csrf_exempt
def send_emails(request):
    api_btc_url = 'https://api.coingecko.com/api/v3/coins/bitcoin?localization=en'
    current_btc_price = requests.request('GET', api_btc_url).json()
    with open('emails.txt', 'r') as emails:
        for email in emails.read().split(" "):
            message = Mail(
                from_email='yourslaveyourbitc4@gmail.com',
                to_emails=f'{email}',
                subject='BTC to UAH price',
                html_content=f"<strong>{current_btc_price['market_data']['current_price']['uah']}</strong>")
            sg = SendGridAPIClient("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")
            response = sg.send(message)
            return JsonResponse({"response": "200",
                                 "description": "Emails were sent"})

