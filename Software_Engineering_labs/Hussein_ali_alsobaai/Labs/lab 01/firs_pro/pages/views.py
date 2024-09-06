from django.shortcuts import render

info={
    "name":["ibrahim","amro"],
    "age":25,
    "city":"Yemen"
}
# Create your views here.
def index(request):
    return render(request,'pages/index.html',info)


def link(request):
    return render(request,'pages/link.html',info)
