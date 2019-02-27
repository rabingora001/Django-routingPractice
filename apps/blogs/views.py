from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display all the list of blogs.")

def new(request):
    x="placeholder to display a new form to create a new blog"
    return HttpResponse(x)

def create(request):
    return redirect('/')

def show(request, number):
    response="placeholder to display blog " + number 
    return    HttpResponse(response)

def edit(request, number):
    response= number +" edit blog"
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')