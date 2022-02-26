from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .models import User


default_bootstrap_classes = 'form-control form-control-lg'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __int__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # Adding Bootstrap classes and placeholders to form fields
        self.fields['username'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['password'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': default_bootstrap_classes,
        'placeholder': "Email Address"
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': default_bootstrap_classes,
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': default_bootstrap_classes,
        'placeholder': 'Last Name'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Old Password',
        'type': 'password',
        'class': default_bootstrap_classes
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'New Password',
        'type': 'password',
        'class': default_bootstrap_classes
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm New Password',
        'type': 'password',
        'class': default_bootstrap_classes
    }))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['class'] = default_bootstrap_classes
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
