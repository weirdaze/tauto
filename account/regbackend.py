from registration.backends.default.views import RegistrationView
from account.forms import UserRegisterForm


class MyRegistrationView(RegistrationView):
    form_class = UserRegisterForm