from django.shortcuts import render
from .person import Person

# Create your views here.
def tem_var(request, name):
    return render(request, "show_var.html", {"name": name})
    # it will display the text after api endpoint as header
    # e.g. http://127.0.0.1:8000/tem_app/var/12345/
    # will show: "12345" as header

def pass_dict(request):
    sample = {
        "name": "Django",
        "teacher": "Dr. Su"
    }
    return render(request, "show_info.html", {"product": sample})

def pass_obj(request):
    rick = Person("Rick", 80)
    return render(request, "show_info.html", {"person": rick})