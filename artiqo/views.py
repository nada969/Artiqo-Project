from django.http import HttpResponseNotFound , HttpResponse

def handler404(request,exception):
    return HttpResponseNotFound('404: page not found! <br><br> <a href="/users/"style="display: inline-block; padding: 5px 10px; background-color: #f0f0f0; text-decoration: none; border: 1px solid #ccc; border-radius: 4px;">Go To Home Page</a>')