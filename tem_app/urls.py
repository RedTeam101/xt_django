from django.urls import path
from tem_app.views import tem_var             # 同目录下的 views.py


urlpatterns = [
    path("var/<name>/", tem_var),
]