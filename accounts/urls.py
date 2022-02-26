from django.urls import path
from . import views


app_name = 'accounts'


urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('login/', views.LoginPageView.as_view(), name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', views.UserEditProfileForm.as_view(), name='account'),
    path('password/', views.PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', views.PasswordSuccessView.as_view(), name='password_success')
]
