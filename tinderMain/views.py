#from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Tinder-Clone App. Joint Project by Debkanta Mondal & Sourav Garai.")
