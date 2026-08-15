import time
from django.shortcuts import render
from .tasks import send_welcome_email


def home(request):
    return render(request, 'emailer/home.html')

def send_bulk_emails(request):
    recipients = [f"user{i}@example.com" for i in range(1, 11)]  # 10 fake recipients

    for email in recipients:
        send_welcome_email.delay(email)

    return render(request, 'emailer/success.html', {'count': len(recipients)})