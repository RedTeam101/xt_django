from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("弯弯的月亮")

def sun(request):
    return HttpResponse("灿烂的太阳")

def star(request):
    return HttpResponse("闪烁的星星")
