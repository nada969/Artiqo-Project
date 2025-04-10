from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages
from product.models import Product
from users.models import Users
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def userRole(request):
    return render(request,'users/base.html')

def home(request):
    products = Product.objects.filter(is_sold=False)
    users = Users.objects.filter(role='Artist',products__is_sold=False).distinct()
    return render(request,'users/home.html',{'products':products , 'users':users})


def profile(request):
    pass

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f' welcome {username} !!')
                return redirect(reverse('home'))
            else:
                messages.info(request, f'account done not exit plz sign in')
    else:
        form = AuthenticationForm()
    return render(request,'users/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(reverse('home'))
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
