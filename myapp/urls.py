from django.urls import path
from . import views             # 同目录下的 views.py

urlpatterns = [
    path('', views.index, name='index'),    # 弯弯的月亮 api
    path('sun/', views.sun, name='sun'),    # 灿烂的太阳 api
    path('star/', views.star, name='star'), # 闪烁的星星 api
]