from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from Newsletter.models import NewsletterUser




def newsletter(request):
  
    if request.method == 'POST':
        email = request.POST['email']
        if NewsletterUser.objects.filter(email=email).exists():
            return redirect('home')
        else:
            new_signup = NewsletterUser()
            new_signup.email = email

            new_signup.save()
          
            send_mail(
                'Welcome to Chain',
                'Thank you for subscribing to our newsletter',
                'mert_gunes2008@hotmail.com',
                [email],
                fail_silently=False,
            )
            return redirect('home')