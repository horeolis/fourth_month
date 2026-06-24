from django.shortcuts import render
from django.http.response  import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1> Hello World!</h1>")


def about(request):
    name = "Islam"
    age = 22
    nickname = "horeolisssuka"

    response = f"<h1>{name}</h1> <br> <h2> {age} </h2> <p> {nickname} </p>"

    return HttpResponse(response)


def image_test(request):
    name = "Zoro"
    age = 21
    lvl = 35

    image = "https://i.pinimg.com/474x/19/24/0e/19240e2580374bae68529aa38dffd392.jpg"

    response = f"<h1>{name}</h1> <br> <h2> {age} </h2> <p> {lvl} </p> <img src='{image}'>"
    return HttpResponse(response)