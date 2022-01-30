from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import json

from .models import User, Post


def index(request):
    if request.method == "POST":
        postContent = request.POST["content"]
        post = Post.objects.create(
            user=request.user,
            content=postContent
        )
        return HttpResponseRedirect(reverse("index"))
    else:
        posts = Post.objects.all().order_by("id").reverse()
        p = Paginator(posts, 10, orphans=0, allow_empty_first_page=True)
        pageNumber = request.GET.get('page')
        pageObj = p.get_page(pageNumber)
        return render(request, "network/index.html", {
            'page_obj': pageObj
        })

@login_required(login_url='/login') 
def following(request):
    followsUser = request.user.follows.all()
    posts = Post.objects.filter(user in followsUser).order_by("id").reverse()
    print(posts)
    return HttpResponse(status=204)




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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def update(request, id):
    if request.method == "PUT":
        data = json.loads(request.body)
        if data["toUpdate"] == "like":
            post = Post.objects.get(pk=id)
            if request.user in post.like.all():
                post.like.remove(request.user)
            else:
                post.like.add(request.user)
            return HttpResponse(status=204)
        elif data["toUpdate"] == "post":
            post = Post.objects.get(pk=id)
            post.content = data["content"]
            post.save()
            print(post.content)
            return HttpResponse(status=204)
        elif data["toUpdate"] == "follow":
            userProfile = User.objects.get(pk=id)
            if userProfile in request.user.follows.all():
                request.user.follows.remove(userProfile)
            else:
                request.user.follows.add(userProfile)
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=404)    
    else:
        return HttpResponse(status=404)


def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all().order_by("id").reverse()
    p = Paginator(posts, 10, orphans=0, allow_empty_first_page=True)
    pageNumber = request.GET.get('page')
    pageObj = p.get_page(pageNumber)
    return render(request, "network/profile.html", {
        'page_obj': pageObj,
        'userProfile': user
    })
    return HttpResponse(status=204)




