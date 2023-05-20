# these to imports are ues to make use sign in page (new ues)
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        # it is like what will show in the label or what the type of the label
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"
