# GSES2-BTC-application



## To send emails you need TO register an account on https://sendgrid.com/ 


## then create and paste your API KEY on btc_price_monitoring/api/views.py, line 62: sg = SendGridAPIClient("YOUR SENDGRID API KEY") 


## After that add your email on line 58: from_email='YOUR EMAIL',



API endpoints: 
## 1. localhost/api


## 2. localhost/api/rate/

#### Shows current BTC to UAH price


## 3. localhost/api/subscription/

#### Takes in a POST request:
#### {'email': 'youremail@example.com'}
##### Have in mind that the application does NOT check if the email you send is valid, so please, use valid emails.


## 4. localhost/api/sendEmail/

#### Sends a message with current BTC to UAH price to every registrated email.



