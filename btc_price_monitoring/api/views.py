import requests

from django.http import JsonResponse

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.views.decorators.csrf import csrf_exempt


def show_paths(request):
    return JsonResponse({'tags': {
        'rate': 'Get the current rate of BTC to UAH',
        'subscription': 'subscribe to newsletter',
	'sendEmails': 'send emails to all subscribed users'
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
                print(e.rstrip())
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
    if request.method == "POST":
        sg = sendgrid.SendGridAPIClient(api_key="YOUR API KEY")
        from_email = Email("YOUR EMAIL")
        subject = "BTC to UAH price"
        content = Content("text/plain", f"{current_btc_price['market_data']['current_price']['uah']}")
        mail = Mail(from_email=from_email, to_emails=None, subject=subject, html_content=content)
        with open('emails.txt', 'r') as emails:
            for e in emails.read().split(" "):
                email = e.rstrip()
		## Creating a list of emails to which the message will be sent. (The recipients of the email will NOT see each others ##
		## emails address in the TO field.) ##
                person = Personalization()
                person.add_to(Email(f"{email}"))
                mail.add_personalization(person)

            mail_json = mail.get()

            response = sg.client.mail.send.post(request_body=mail_json)

            return JsonResponse({"response": "200",
                                 "description": "Emails were sent"})


