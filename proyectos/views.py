import json
from django import forms

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import *


# Form to request quote
class RequestQuoteForm(forms.Form):
    project_name = forms.CharField(label="Nombre de proyecto")
    # type (Asesoria, asistencia, elaboracion)
    deadline = forms.DateField()
    university = forms.CharField(label="Universidad")
    aspirated_degree = forms.CharField(label="Grado al que aspira")
    country = forms.CharField(label="País")
    name = forms.CharField(label="Nombre del solicitante")
    additional_information = forms.CharField(
        label="Información adicional", 
        widget=forms.Textarea
    )
    attach = forms.FileField(label="Adjunte Archivo")

    


# Create your views here.
def index(request):
    return render(request, "proyectos/index.html")


def login_view(request):
    # User reached route via POST
    if request.method == "POST":
        # Get data submitted and attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful, and login
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "proyectos/login.html", {
                "message": "Invalid username and/or password",
                "alert": "alert-warning"
            })
        
    else:
        # User reached route via GET
        return render(request, "proyectos/login.html")
    

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse("index"))


def register(request):
    # User reached route via POST
    if request.method == "POST":
        # Get data submitted
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        # Make sure that no empty fields were received
        if username == "" or email == "" or password == "" or confirmation == "" or first_name == "" or last_name == "":
            return render(request, "proyectos/register.html", {
                "message": "Debe completar todos los campos.",
                "username": username,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "alert": "alert-warning"
            })

        # Make sure password matches confirmation
        if password != confirmation:
            return render(request, "proyectos/register.html", {
                "message": "La contraseña y su confirmación deben coincidir.",
                "username": username,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "alert": "alert-warning"
            })
        
        # Attempt to create a new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        
        except IntegrityError:
            return render(request, "proyectos/register.html", {
                "message": "El nombre de usuario ya existe.",
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "alert": "alert-warning"
            })
        
        # User login, and redirect to index page
        login(request, user)

        return HttpResponseRedirect(reverse("index"))

    else:
        # User reached route via GET
        return render(request, "proyectos/register.html")
        

def request_quote(request):
    # User reached route via POST
    if request.method == "POST":
        pass

    else:
        # User reached route via GET
        return render(request, "proyectos/request_quote.html", {
            "form": RequestQuoteForm()
        })

    return


def services(request):
    return render(request, "proyectos/services.html")

