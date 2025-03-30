from django.shortcuts import render

# Create your views here.
def neworderart(request):
    return render(request,'order/neworderart.html')