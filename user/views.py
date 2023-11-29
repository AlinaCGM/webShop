from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.forms import UserRegistrationForm,AddressRegistrationForm

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if user:            
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('user:registration'))
            else:
                return HttpResponse('Account not active')

        else:
            print('Someone tried to login and failed')
            print('Username: {} and password {}'.format(email, password))
            return HttpResponse('Invalid login details supplied')

    else:
        return render(request, 'login.html', {})


def login_view(request):
    return render(request, 'login.html')


def registration(request):
    registered = False
    user_registration_form = UserRegistrationForm(data=request.POST)
    address_registration_form=AddressRegistrationForm(data=request.POST)

    if user_registration_form.is_valid() and  address_registration_form.is_valid():
        address =address_registration_form.save(commit=False)
        address.save()

        user = user_registration_form.save(commit=False)
        user.address=address
        user.set_password(user.password)
        user.save()

        registered = True

    else:
        print(user_registration_form.errors,address_registration_form.errors)

    user_registration_form = UserRegistrationForm()
    address_registration_form=AddressRegistrationForm()

    return render(request, 'registration.html', {'user_form': user_registration_form,
                                                 'address_form':address_registration_form,
                                                      'registered': registered})
