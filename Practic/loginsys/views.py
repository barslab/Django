from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from loginsys.forms import MyRegistrationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/lk')
        else:
            args['login_error'] = "Пользователь c такой парой не найден"
            return render_to_response('login.html', args)
    else:
        args['username'] = auth.get_user(request).username
        # args['first_name'] = auth.get_user(request).first_name
        # args['last_name'] = auth.get_user(request).last_name
        return render_to_response('login.html', args)
def logout(request):
    auth.logout(request)
    return redirect("/login/")


def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            newuser = auth.authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password2'])
            auth.login(request, newuser)
            return HttpResponseRedirect('/')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print(args)
    return render(request, 'register.html', args)

def lk(request):
    username = auth.get_user(request).username
    return render_to_response('lk.html', { 'username': username })