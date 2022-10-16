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
    allCategories = Category.objects.all()
    context = {
        "listing": listing,
        "categories": allCategories,
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
def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    return render(request, "auctions/listing.html", {
        "listing": listingData
    })

def createListing(request):
    if request.method == "GET":
        allCategories = Category.objects.all()
        return render(request, "auctions/create.html", {
            "categories":allCategories
        })
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        imageURL = request.POST["imageURL"]
        price = request.POST["price"]
        category = request.POST["category"]
        categoryData = Category.objects.get(categoryName=category)
        #WHO IS USER
        currentUser = request.user
        newListing = Listing(
            title=title,
            description=description,
            imageURL=imageURL,
            price=price,
            category=categoryData
        )
        newListing.save()
        return HttpResponseRedirect(reverse("index"))
def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
        activeListings = Listing.objects.filter(isActive=True, category=category)
        allCategories = Category.objects.all()
        return render(request, "auctions/index.html", {
            "listing": activeListings,
            "categories": allCategories,
        })

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