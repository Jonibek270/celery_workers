from celery import shared_task
from .send_otp import send_otp_mail
@shared_task
def send_email_task(email,otp):
    send_otp_mail(email,otp)
    return f"Email sent to {email}"