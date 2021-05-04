import requests




class User():
    """
    Main users api class to handle comunication with the users service
    """
    
    def __init__(self) -> None:
        self.__USERS_SERVICE_URL = "http://localhost:5100/"
    
    def __repr__(self):
        return "User()"

    def create_user(self, form) -> int:
        """
        Request creation of a new user to the Users service.
        form: instance of RegisterForm with user data
        return: 200 if response OK or error code if not OK
        """
        # endpoint
        self.__register_url = self.__USERS_SERVICE_URL + "user/register/"
        # instance of request session to handle requests of csrf token
        # as normal requests.get and requests.post methods don't keep track of csrf cookies
        # used by django views
        self.__req_session = requests.session()
        # get csrf_token from remote url
        self.__csrf_token = self.__req_session.get(self.__register_url)
        # request headers
        self.__headers = {
            'X-CSRFToken': self.__csrf_token.cookies.get("csrftoken")
        }
        # data to send in the request
        self.__data = {
            "first": form.first.data,
            "last": form.last.data,
            "email": form.email.data,
            "phone": form.phone.data,
            "address": form.address.data,
            "zip_code": form.zip_code.data,
            "country": form.country.data,
            "password": form.password.data,
        }
        # make requests
        self.__response = self.__req_session.post(self.__register_url, headers=self.__headers, data=self.__data)
        # if user was registered
        if self.__response.ok and self.__response.status_code == 200:
            return 200
        return self.__response.reason

    def login(self, form):
        # instance of request session
        self.__session = requests.session()
        # get session csrf_token from remote url
        self.__response = self.__session.get(self.__USERS_SERVICE_URL + "user/login/")
        # if csrf token retrieved
        if self.__response.ok and self.__response.status_code == 200:
            # get token from response
            self.__csrf_token = self.__response.cookies.get("csrftoken")
            # get form data
            self.__data = {
                "username": form.email.data,
                "password": form.password.data
            }
            # declare post request headers
            self.__headers = {
                "X-CSRFToken": self.__csrf_token
            }
            # make request
            self.__response = self.__session.post(self.__USERS_SERVICE_URL + "user/login/",
                                                    headers=self.__headers,
                                                    data=self.__data)
            # if user authenticated
            if self.__response.ok and self.__response.status_code == 200:
                # RETURN THE JWT HERE
                return self.__response
        return None











