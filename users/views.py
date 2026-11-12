from django.shortcuts import render, redirect
from .forms import RegisterForm , VerifyOTPForm
from .models import CustomUser, UserOTP
from django.contrib import messages
from .utilis import generate_otp
from .send_otp import send_otp_mail
from .tasks import send_email_task

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            otp = generate_otp()
            UserOTP.objects.create(user=user, otp=otp)
            email=user.email
            send_email_task.delay(email,otp)
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz")
            return redirect('verify_otp')

    form = RegisterForm()
    context = {"form": form}
    return render(request, "users/register.html", context)

def verify_otp_view(request):
    if request.method == "POST":
        form= VerifyOTPForm(request.POST or None)
        if form.is_valid():
          otp=form.cleaned_data["otp"]
        user_otp = UserOTP.objects.filter(otp=otp).first()
        if user_otp:
            user_otp.is_active = True
            user_otp.is_used = True
            user_otp.save()
            messages.success(request,'Sizning akkountingiz tasdiqlandi')
            return redirect('login')

    form=VerifyOTPForm()
    context = {"form": form}
    return render(request, "users/verify_otp.html", context)
