from django.shortcuts import render
from django .http import HttpResponse
def testpaper(request):
    s="<h1>This is your test Paper</h1>"
    return HttpResponse(s)
def result(request):
    s="<h1>This is your test result</h1>"
    return HttpResponse(s)