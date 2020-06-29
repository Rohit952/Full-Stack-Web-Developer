from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'testapp1/index.html',{ 'template': 'hello'})
