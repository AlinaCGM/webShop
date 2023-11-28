from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            print('authenticated')
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('user:login_view'))
            else:
                return HttpResponse('Account not active')

        else:
            print('Someone tried to login and failed')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('Invalid login details supplied')

    else:
        return render(request, 'login.html', {})
    
def login_view(request):
    return render(request,'login.html')