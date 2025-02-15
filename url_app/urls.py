from django.urls import path
from url_app.views import go_reverse, get_url, show_hobby, get_reverse

app_name = 'url'

urlpatterns = [
    path("reverse/",go_reverse, name="reverse"),
    path("hello/", get_url, name="hello"),
    path("show/<fruit>/<sport>", show_hobby, name="show"),
    path("view/", get_reverse, name="view"),
]