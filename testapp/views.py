from django.shortcuts import render
from django.http import HttpResponse
def greetings(request):
    s="<h1>hello and I'm Ashish Prabhakar</h1> "
    return HttpResponse(s)
def about(request):
    s="<h1>About/h1> "
    return HttpResponse(s)
def contact(request):
    s="<h1>Contact Page</h1> "
    return HttpResponse(s)