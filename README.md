# GSES2-BTC-application



## TO SEND EMAILS YOU NEED TO REGISTER AN ACCOUNT ON https://sendgrid.com/ 


## AND PASTE YOUR API KEY on btc_price_monitoring/api/views.py, line 62: sg = SendGridAPIClient("YOUR SENDGRID API KEY") 


## Then add your email on line 58: from_email='YOUR EMAIL',



API endpoints: 
## 1. localhost/api


## 2. localhost/api/rate/

#### Shows current BTC to UAH price


## 3. localhost/api/subscription/

#### Takes in a POST request 
#### {'email': 'youremail@example.com'}


## 4. localhost/api/sendEmail/

#### Sends a message with current BTC to UAH price to every registrated email.



