from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'account/index.html')


def sample(request):
    return render(request, 'account/sample.html')

