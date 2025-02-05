from django.urls import path
# from tem_app.views import tem_var                     # 同目录下的 views.py
from tem_app.views import tem_var, pass_dict, pass_obj  # 导入多个 views 时用逗号分隔

urlpatterns = [
    path("var/<name>/", tem_var),
    path("dict/", pass_dict),
    path("obj/", pass_obj),
]