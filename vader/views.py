from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Congrats</h1><div><img src="/static/pic.jpg"></img></div>')
