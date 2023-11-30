from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from user.forms import UserRegistrationForm, AddressRegistrationForm, UserProfileForm, AddressForm

# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("user:profile"))
            else:
                return HttpResponse("Account not active")

        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, "login.html", {})


def registration(request):
    registered = False
    user_registration_form = UserRegistrationForm(data=request.POST)
    address_registration_form = AddressRegistrationForm(data=request.POST)

    if user_registration_form.is_valid() and address_registration_form.is_valid():
        address = address_registration_form.save(commit=False)
        address.save()

        user = user_registration_form.save(commit=False)
        user.address = address
        user.set_password(user.password)
        user.save()

        registered = True

    else:
        print(user_registration_form.errors, address_registration_form.errors)

    user_registration_form = UserRegistrationForm()
    address_registration_form = AddressRegistrationForm()

    return render(
        request,
        "registration.html",
        {
            "user_form": user_registration_form,
            "address_form":  address_registration_form,
       "registered": registered,
        },
    )


@login_required
def profile(request):
    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=request.user.address)

        if address_form.is_valid():
            address_form.save()           

            messages.success(request, 'Your address successfully updated.')
            return redirect('user:profile')
    else:
        user_form = UserProfileForm(instance=request.user)
        address_form = AddressForm(instance=request.user.address)

    return render(request, 'profile.html', {'user_form': user_form, 'address_form': address_form})
