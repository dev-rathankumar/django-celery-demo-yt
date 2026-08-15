from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_welcome_email(to_email):
    print('Sending to: ', to_email)
    send_mail(
        subject="Welcome!",
        message="Thanks for signing up.",
        from_email=None,
        recipient_list=[to_email],
    )
    return f"Sent to {to_email}"
