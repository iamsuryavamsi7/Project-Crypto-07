from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.info(request, "Passwords not matching")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already taken")
            return redirect("register")
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect("register")
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                            email=email, password=password2)
            user.save()
            return redirect("login")

    else:
        return render(request, "register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")

    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
