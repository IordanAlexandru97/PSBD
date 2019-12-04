from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Patient

posts = [
    {
        'author': 'Iordan Alexandru',
        'title': 'About the application',
        'content': 'content',
        'date_posted': '12th of Dec 2019'
     },
    {
        'author': 'Jane Doe',
        'title': 'Post number 2',
        'content': 'Second post content',
        'date_posted': '13th of Dec 2019'
     },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'website/home.html', context)


def about(request):
    return render(request, 'website/about.html',{'title':'About'})

