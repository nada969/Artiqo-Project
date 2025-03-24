from django.shortcuts import render

# Create your views here.
def userRole(request):
    return render(request,'users/base.html')