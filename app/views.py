from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate

from app.models import Product

User = get_user_model()


def index(request):
    products = Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request, 'index.html', ctx)


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        parol = request.POST['parol']

        if User.objects.filter(username=username).exists():
            return render(request, 'include/base.html', {'error': 'Username already exists'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'include/base.html', {'error': 'Email already exists'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.parol = parol
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to the home page or any other page
    else:
        return render(request, 'include/base.html')
