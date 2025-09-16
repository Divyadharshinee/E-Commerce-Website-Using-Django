from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# 🔹 Register View
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Username already exists")
            return redirect("register")

        # create user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "✅ Account created successfully. Please login.")
        return redirect("login")

    return render(request, "register.html")


# 🔹 Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}! 🎉")
            return redirect("shop_home")   # redirect to product list
        else:
            messages.error(request, "❌ Invalid username or password")
            return redirect("login")

    # 👇 IMPORTANT: for GET requests, just show login page
    return render(request, "login.html")



# 🔹 Logout View
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")
