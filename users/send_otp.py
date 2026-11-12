from django.conf import settings
from django.core.mail import send_mail

def send_otp_mail(email, otp):
    send_mail(
        subject="Axrorcloud - Tasdiqlash kodi",
        message=f"Assalomu aleykum Sizning tasdiqlash kodingiz: {otp}",
        from_email="nozimbek924@gmail.com",
        recipient_list=[email],
    )
    return f"email sent to {email}"