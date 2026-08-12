import time
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'emailer/home.html')

def send_bulk_emails(request):
    recipients = [f"user{i}@example.com" for i in range(1, 11)]  # 10 fake recipients

    for email in recipients:
        print('Sending to: ', email)
        time.sleep(1)  # simulate slow send
        send_mail(
            subject="Welcome!",
            message="Thanks for signing up.",
            from_email=None,  # falls back to DEFAULT_FROM_EMAIL
            recipient_list=[email],
        )

    return render(request, 'emailer/success.html', {'count': len(recipients)})