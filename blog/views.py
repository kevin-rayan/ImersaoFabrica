from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def chiclete (request):
    return render(request, template_name='blog/home.html')