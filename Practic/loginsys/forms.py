from django import forms

# class SignupForm(forms.Form):
#     firstname = forms.CharField(label=u'Имя пользователя')
#     lastname = forms.CharField(label=u'Фамилия пользователя')
#     number = forms.CharField(label=u'Номер группы')
#     username = forms.CharField(label=u'Логин')
#     password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput())
#     password2 = forms.CharField(label=u'Повторите пароль', widget=forms.PasswordInput())
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User  # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import request

from loginsys.models import UserProfile


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    group_number = forms.CharField(required=True)
    # birtday = forms.DateField(required = False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'group_number')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.group_number = self.cleaned_data['group_number']

        # user.birthday = self.cleaned_data['birthday']
        if commit:
            user.save()
        return user
