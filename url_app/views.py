from django.shortcuts import render, redirect
from django.http import (
    HttpResponse,          # 基本的HTTP响应
    JsonResponse,          # 返回JSON数据
    HttpResponseRedirect,  # HTTP重定向
    HttpResponseNotFound,  # 404错误
    HttpResponseBadRequest,# 400错误
    HttpResponseForbidden,# 403错误
    HttpResponseServerError,# 500错误
)
from django.urls import reverse

# Create your views here.
def go_reverse(request):
    return render(request,"reverse.html")



def get_url(request):
    return render(request,"hello.html")

def show_hobby(request, fruit,sport):
    msg = f"my favorite fruit is {fruit}; my favorite sport is {sport}"
    return HttpResponse(f"<h3>{msg}</h3>")

def get_reverse(request):
    fruit = "Banana"
    sport = "Skydiving"
    #eturn redirect(reverse("url:show",args=(fruit, sport)))
    return redirect(reverse("url:show",kwgs={"fruit":fruit, "sport": sport}))