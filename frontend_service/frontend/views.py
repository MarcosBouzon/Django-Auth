from .api.user import User
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.shortcuts import redirect, render

# Create your views here.

def login(request):
    # instance of login form
    login_form = LoginForm()
    if request.method == "POST":
        # get posted data in form
        data = request.POST
        login_form = LoginForm(data)
        # check if form is valid
        if login_form.validate():
            # request user login
            user = User().login(login_form)
            if not user:
                # form is invalid
                messages.error(request, "Invalid credentials, please check spelling")
                return redirect("frontend_login")
            # user authenticated successfully
            messages.success(request, "Welcome back")
            return redirect("frontend_login")
        # form is invalid
        messages.error(request, "Invalid credentials, please check spelling")
    context = {
        "form": login_form,
    }
    return render(request, "frontend/login.html", context)

def register(request):
    # instance of login form
    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.validate():
            # instance of user class
            user = User()
            # request user registration
            registered = user.create_user(register_form)
            if registered == 200:
                # send success message
                messages.success(request, "You have been successfully registered")
            # user wasn't created
            else:
                messages.error(request, registered)
            return redirect(register)

    # context dict
    context = {
        "form": register_form
    }
    return render(request, "frontend/register.html", context)




