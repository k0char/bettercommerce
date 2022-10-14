from xml.dom import xmlbuilder
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from .models import User, Item, Categories


def index(request):
    items = Item.objects.all().values()
    template = loader.get_template("auctions/index.html")
    context = {
        "items": items,
    }
    return HttpResponse(template.render(context, request))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
def create(request):
    template = loader.get_template("auctions/create.html")
    return HttpResponse(template.render({}, request))
def createrecord(request):
    x = request.POST["name"]
    y = request.POST["price"]
    z = request.POST["description"]
    item = Item(name=x, price=y, description=z)
    item.save()
    return HttpResponseRedirect(reverse("index"))
def categories(request):
    categories = Categories.objects.all().values()
    template = loader.get_template("auctions/categories.html")
    context = {
        "categories": categories,
    }
    return HttpResponse(template.render(context, request))
def addcategory(request):
    template = loader.get_template("auctions/addcategory.html")
    return HttpResponse(template.render({}, request))
def addcategoryrecord(request):
    x = request.POST["name"]
    category = Categories(name=x)
    category.save()
    return HttpResponseRedirect(reverse("auctions/category.html"))