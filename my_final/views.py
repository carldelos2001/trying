from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserExtend,RequestBlood,BloodGroup
from .forms import UserForm1, UserForm2, LoginForm, RequestForm, ChangeForm1, ChangeForm2, UserForm3
from django.db.models import Count
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserExtendForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def editRequestView(request):
    # Get the requests for the logged-in user
    user_requests = RequestBlood.objects.filter(user=request.user)

    if request.method == "POST":
        form = RequestForm(request.POST)

        if form.is_valid():
            # Assuming there's a form field like 'request_id' to identify the specific request
            request_id = form.cleaned_data.get('request_id')
            obj = get_object_or_404(RequestBlood, id=request_id, user=request.user)
            form = RequestForm(request.POST, instance=obj)

            if form.is_valid():
                form.save()
                return redirect('allrequest')
    else:
        form = RequestForm()

    return render(request, 'edit_request.html', {'form': form, 'user_requests': user_requests})
@login_required
def available(request):
    all_group = BloodGroup.objects.annotate(total=Count('userextend'))
    return render(request, 'available.html',{"all_group":all_group})

def my_final(request):
    return HttpResponse("Hello world!")

def welcome(request):
    return render(request, 'home.html')

def registerView(request):
    if request.method == "POST":
        form1 = UserForm1(request.POST)
        form2 = UserForm2(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.set_password(obj.password)
            obj.save()
            obj2 = form2.save(commit=False)
            obj2.donor = obj
            obj2.save()
            return redirect('login')
    else:
        form1 = UserForm1()
        form2 = UserForm2()

    return render(request, 'register.html', {'form1':form1,'form2':form2})
def patientView(request):
    if request.method == "POST":
        form1 = UserForm1(request.POST)
        form3 = UserForm3(request.POST, request.FILES)
        if form1.is_valid() and form3.is_valid():
            obj = form1.save(commit=False)
            obj.set_password(obj.password)
            obj.save()
            obj2 = form3.save(commit=False)
            obj2.donor = obj
            obj2.save()
            return redirect('login')
    else:
        form1 = UserForm1()
        form3 = UserForm3()

    return render(request, 'patientreg.html', {'form1':form1,'form3':form3})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['user_type']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Perform authentication based on user_type (donor or patient)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user_type == 'donor':
                    # Handle donor login logic
                    # For example: redirect to donor dashboard
                    login(request, user)
                    return render(request, 'donor.html')
                elif user_type == 'patient':
                    # Handle patient login logic
                    # For example: redirect to patient dashboard
                    login(request, user)
                    return render(request, 'patient.html')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
# Create your views here.

@login_required
def changePasswordView(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
        
    return render(request, 'password.html', {'form':form})
def loginFirst(request):
    return render(request, 'login_first.html')

def changePasswordOrLoginView(request):
    if request.user.is_authenticated:
        return changePasswordView(request)
    else:
        return loginFirst(request)
    
@login_required   
def createReqView(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allrequest')
    else:
        form = RequestForm()

    return render(request, 'createrequest.html', {'form':form})
@login_required
def allReqView(request):
    all_req = RequestBlood.objects.all()
    return render(request, 'allrequest.html', {'all_req':all_req})

def detailView(request, id):
    obj = get_object_or_404(User, pk=id)
    return render(request, 'details.html', {'obj':obj})

def groupView(request, id):
    obj = get_object_or_404(BloodGroup, pk=id)
    donor = UserExtend.objects.filter(blood_group=obj)
    return render(request, 'donorlist.html', {'donor':donor})


@login_required
def profileView(request):
    return render(request, 'profile.html')

@login_required
def editProfileView(request):
    try:
        user_extend_instance = request.user.userextend
    except UserExtend.DoesNotExist:
        user_extend_instance = None

    if request.method == "POST":
        form1 = ChangeForm1(request.POST, instance=request.user)
        form2 = ChangeForm2(request.POST, request.FILES, instance=user_extend_instance)
        if form1.is_valid() and form2.is_valid():
            obj = form1.save()
            if user_extend_instance:
                obj2 = form2.save(commit=False)
                obj2.donor = obj
                obj2.save()
            return redirect('profile')
    else:
        form1 = ChangeForm1(instance=request.user)
        form2 = ChangeForm2(instance=user_extend_instance)

    return render(request, 'edit_profile.html', {'form1': form1, 'form2': form2})
@login_required
def donor_dashboard(request):
    all_request = RequestBlood.objects.filter(name=request.user)
    print(all_request)  # Add this to verify the content in console/terminal
    return render(request, 'donor.html', {'allrequest': all_request})


@login_required
def getRequestView(request):
    if request.method == "POST":
        pin = request.POST.get("pin")
        obj = get_object_or_404(RequestBlood, pin_code=int(pin))
        return render(request, 'get_request.html',{'obj':obj})

    return render(request, 'get_request.html')

def deleteRequestView(request, pin):
    obj = get_object_or_404(RequestBlood, pin_code=pin)
    obj.delete()
    return redirect('allrequest')

def logoutView(request):
    logout(request)
    return redirect('home')

@login_required
def statusView(request):
    user_extend = get_object_or_404(UserExtend, donor=request.user)

    # If the user has ready_to_donate as False, delete them from the database
    if not user_extend.ready_to_donate:
        user_extend.delete()
        # Redirect to a page or URL after deletion
        return HttpResponseRedirect(reverse('available'))

    # Update the ready_to_donate status to False
    user_extend.ready_to_donate = False
    user_extend.save()

    # Render the updated profile page
    return render(request, 'available.html', {'user_extend': user_extend})

def user_extend_form_view(request):
    if request.method == 'POST':
        form = UserExtendForm(request.POST)
        if form.is_valid():
            # Process the form data if valid
            form.save()
            # Redirect or perform necessary actions
    else:
        form = UserExtendForm()

    return render(request, 'register.html', {'form': form})

def patient_dashboard(request):
    return render (request, 'patient.html'); 

