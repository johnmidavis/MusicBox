from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("great - we got an album thing")

# Create your views here.
