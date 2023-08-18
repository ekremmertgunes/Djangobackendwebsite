from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('Email addresses must be unique.')
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name and User.objects.filter(first_name=first_name).count():
            raise forms.ValidationError('First Name must be unique.')
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and User.objects.filter(last_name=last_name).count():
            raise forms.ValidationError('Last Name must be unique.')
        return last_name

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user