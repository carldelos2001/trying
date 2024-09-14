from django import forms
from django.contrib.auth.models import User
from .models import UserExtend, RequestBlood, UserExtend2
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserForm1(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        widgets = {
            'password': forms.PasswordInput,
        }

class UserForm2(forms.ModelForm):
    class Meta:
        model = UserExtend
        exclude = ('donor','ready_to_donate')

class UserForm3(forms.ModelForm):
    class Meta:
        model = UserExtend2
        exclude = ('patient','need_donation')

class UserExtend2Form(forms.ModelForm):
    class Meta:
        model = UserExtend2
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.SelectDateWidget(),
        }



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    user_type = forms.ChoiceField(choices=(('donor', 'Donor'), ('patient', 'Patient')))
   

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestBlood
        fields = "__all__"


class ChangeForm1(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class ChangeForm2(forms.ModelForm):
    class Meta:
        model = UserExtend
        exclude = ('donor','ready_to_donate')

class ChangeForm3(forms.ModelForm):
    class Meta:
        model = UserExtend2
        exclude = ('patient','need_donation')


class UserExtendForm(forms.ModelForm):
    class Meta:
        model = UserExtend
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.SelectDateWidget(),
        }


  

 
   
