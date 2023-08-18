from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.conf import settings
from django.template.loader import get_template
from .models import BuildPackets 
from django.contrib.auth.models import User
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from account.forms import SignUpForm as UserCreationForm
from .models import Services, About, Comments, BuildPackets,UserPackets
from django.contrib.auth import views as auth_views

def home(request):
    return render(request, 'home.html')
def services(request):
 return render (request, 'services.html')
def about(request):
    return render (request, 'about.html')
def pricing (request):
    build_packets=BuildPackets.objects.all()
    return render(request, 'pricing.html',{"build_packets":build_packets})


def newsletterpage(request):
 return render(request, 'newsletter.html')
        
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            form = AuthenticationForm()
            return render(request=request, template_name="login.html", context={"form":form})
    else:
        form = AuthenticationForm()
        return render(request=request, template_name="login.html", context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

def payment(request, id):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        id = id
        return render(request, 'payment.html', {"id":id})
    else:
        id = id
        user = request.user
        packet = BuildPackets.objects.get(id=id)
        # if user has already bought this packet just it can bought another packet this packet was deleted
        user_packet = UserPackets.objects.filter(user=user, packet=packet).first()
        user_packets= UserPackets.objects.filter(user=user)
        # if user has already bought this packet just it can bought another packet this packet was deleted
        if user_packet:
            return render(request, 'payment.html', {"id":id,"message":"You have already bought a packet","error_class":"alert-danger"})
        else:
            # if user has bought another packet this packet was deleted
            if user_packets:
                for user_packet in user_packets:
                    user_packet.delete()
            user_packet = UserPackets.objects.create(user=user, packet=packet)
            user_packet.save()
            return render(request, 'payment.html', {"id":id,"message":"You have bought a packet","error_class":"alert-success"})

def userprofile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    user = request.user
    user_packet = UserPackets.objects.filter(user=user).first()
    return render(request, 'userprofile.html', {"user_packet":user_packet})
       
