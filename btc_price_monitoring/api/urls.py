from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_paths, name='all-commands'),
    path('rate/', views.current_rate, name='current-rate'),
    path('subscription/', views.add_email, name='subscribe'),
    path('sendEmails/', views.send_emails, name='send-emails')

]