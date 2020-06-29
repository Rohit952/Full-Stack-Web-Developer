from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Marks

# Create your views here.
# class listview1(ListView):
#     model = Marks

def index(request):
    data = Marks.objects.all()
    return render(request, 'testapp/marks_list.html', {"data":data})