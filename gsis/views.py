
from django.shortcuts import render, redirect
from django.template.loader import render_to_string, get_template
from .forms import LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm,AdministratorRegistrationForm, StaffRegistrationForm, StudentRegistrationForm, RegistrationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout, authenticate,login


from django.contrib.auth.decorators import login_required

from .models import *

def index(request):
  if not request.user.is_authenticated:
    return redirect("login/")
  else:
    context = {
      'segment'  : 'index',
      #'products' : Product.objects.all()
    }
    return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.administrator:
                login(request, user)
                return redirect('/administrator/home')
            elif user is not None and user.staff:
                login(request, user)
                return redirect('/staff/home')
            elif user is not None and user.student:
                login(request, user)
                return redirect('/student/home')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/auth-signin.html', {'form': form, 'msg': msg})

class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'

def register_administrator(request):
    msg = None
    success = False
    if request.method == "POST":
        form = AdministratorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = AdministratorRegistrationForm()
    
    return render(request, 'accounts/auth-signup.html',{"form": form, "msg": msg, "success": success})

def register_staff(request):
    msg = None
    success = False

    if request.method == "POST":
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = StaffRegistrationForm()
    
    return render(request, 'accounts/auth-signup.html',{"form": form, "msg": msg, "success": success})

def register_student(request):
    msg = None
    success = False

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            return redirect("login")

        else:
            msg = 'Form is not valid'
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'accounts/auth-signup.html',{"form": form, "msg": msg, "success": success})

def logout_view(request):
  logout(request)
  return redirect('login/')

def administrator(request):
    
    return render(request, 'administrator/admnstr_home.html')

def staff(request):
    
    return render(request, 'staff/staff_home.html')

def student(request):
    
    return render(request, 'student/student_home.html')