from .models import UserDetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect, csrf_exempt, ensure_csrf_cookie



# user registration
@ensure_csrf_cookie
def register(request) -> HttpResponse:
    """
    Registers a user in the users model if the user doesn't exist
    return: HttpResponse with operation result
    """
    if request.method == "POST":
        # get data sent in request
        user_data = request.POST
        # check if user exist
        if User.objects.filter(email=user_data.get("email")).first():
            response = HttpResponse(request)
            response.status_code = 403
            response.reason_phrase = "An user with that email already exists. Did you forgot your password?"
            return response
        # register user
        else:
            new_user = User.objects.create_user(first_name=user_data.get("first").lower(), last_name=user_data.get("last").lower(), username=user_data.get("email").lower(),
                            email=user_data.get("email").lower(), password=user_data.get("password"))
            new_user_details = UserDetails(user=new_user, phone=user_data.get("phone"), address=user_data.get("address").lower(), zip_code=user_data.get("zip_code"),
                            country=user_data.get("country").lower())
            # save user
            new_user.save()
            new_user_details.save()
    
        return HttpResponse(request)
    
    # if get request, return csrf_token
    return HttpResponse(request, get_token(request))

# user login
@ensure_csrf_cookie
def user_login(request) -> HttpResponse:
    if request.method == "POST":
        # get post data
        username = request.POST.get("username")
        password = request.POST.get("password")
        # try to authenticate user
        user = authenticate(request, username=username, password=password)
        # invalid credentials
        if not user:
            response = HttpResponse(request)
            response.status_code = 403
            response.reason_phrase = "Invalid credentials"
            return response
        # login user
        login(request, user)
        # GENERATION OF JWT GOES HERE AND RESPONSE MUST RETURN A JWT ACCESS TOKEN

        # user authenticated
        response = HttpResponse(request)
        return response

    # return csrf cookie
    return  HttpResponse(request, get_token(request))












