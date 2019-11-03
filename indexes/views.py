from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "indexes/welcome.html")

def index(request):
    return render(request, 'indexes/index.html')

def detail(request):
    return render(request, "indexes/detail.html")