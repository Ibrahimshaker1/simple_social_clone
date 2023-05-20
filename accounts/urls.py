from django.urls import path
# django have a login view and logout view in django.contrib.auth import views
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"
urlpatterns = [
    # it is the django LoginView you jast neet a html to put it in template_name
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('Logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("signup/", views.SingUp.as_view(), name="signup")
]

