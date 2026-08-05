from django.shortcuts import render
from .models import Student


# Create your views here.
def intex(request):
    import datetime

    context = {
        "title": "My Home Page",
    }
    # students = Student.objects.all()
    # context["students"] = students
    context["students"] = Student.objects.all().order_by("st_id")

    context["date"] = datetime.date.today()
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
