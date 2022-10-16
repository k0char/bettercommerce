from xml.dom import xmlbuilder
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from .models import Listing, Category, User


def index(request):
    listing = Listing.objects.all().values()
    template = loader.get_template("auctions/index.html")
    context = {
        "listing": listing,
    }
    return HttpResponse(template.render(context, request))
"""def index(request):
    items = Item.objects.all().values()
    template = loader.get_template("auctions/index.html")
    context = {
        "items": items,
    }
    return HttpResponse(template.render(context, request))
"""
def createListing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "auctions/create.html", {
            "categories":allCategories
        })
    else:
        a = request.POST["title"]
        b = request.POST["description"]
        c = request.POST["imageURL"]
        d = request.POST["price"]
        e = request.POST["category"]
        categoryData = Category.objects.get(categoryName=e)
        #WHO IS USER
        currentUser = request.user
        listing = Listing(title=a, description=b, imageURL=c, price=d, category=categoryData)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
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