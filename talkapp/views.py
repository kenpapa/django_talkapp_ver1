from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from django.conf import settings
import time
import os

UPLOAD_DIR = settings.STATICFILES_DIRS[0] + '/images/'

def home(request):
    return render(request, 'talkapp/home.html')


def user_create(request):
    return render(request, 'talkapp/user_create.html')

def user_store(request):
    username = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["password"]

    user = User.objects.create_user(username, email, password)
    user.save()

    now = time.time()
    image_file = request.FILES['file']
    path = UPLOAD_DIR + str(now) + image_file.name
    destination = open(path, 'wb+')
    for chunk in image_file.chunks():
        destination.write(chunk)
    destination.close()

    profile = Profile()
    profile.image = str(now) + image_file.name
    profile.user = user
    profile.save()

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)

    return redirect('post_index')

def user_edit(request):
    user = request.user
    context = {
        'user' : user
    }
    return render(request, 'talkapp/user_edit.html', context)

def user_update(request):
    user = request.user

    if request.POST["name"] != '':
        user.username = request.POST["name"]
    if request.POST["email"] != '':
        user.email = request.POST["email"]
    if request.POST["password"] != '':
        user.set_password(request.POST["password"])

    user.save()

    if 'file' in request.FILES:
        old_image_file = UPLOAD_DIR + user.profile.image
        os.remove(old_image_file)

        now = time.time()
        image_file = request.FILES['file']
        path = UPLOAD_DIR + str(now) + image_file.name
        destination = open(path, 'wb+')
        for chunk in image_file.chunks():
            destination.write(chunk)
        destination.close()

        user.profile.image = str(now) + image_file.name
        user.profile.save()

    if request.POST["password"] != '':
        user = authenticate(username=user.username, password=request.POST["password"])
        if user is not None:
            if user.is_active:
                login(request, user)

    return redirect('post_index')


def post_index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'talkapp/post_index.html', context)

def post_create(request):
    return render(request, 'talkapp/post_create.html')

def post_store(request):
    post = Post()
    post.message = request.POST["message"]
    post.user = request.user
    post.save()

    return redirect('post_index')

def post_delete_all(request):
    Post.objects.all().delete()

    return redirect('post_index')


def getLogin(request):
    return render(request, 'talkapp/getlogin.html')

def postLogin(request):
    email = request.POST['email']
    password = request.POST['password']

    try:
       username = User.objects.get(email=email).username
    except User.DoesNotExist:
       username = None

    if username is not None:
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('post_index')

    return render(request, 'talkapp/getlogin.html')

def getLogout(request):
    logout(request)
    return render(request, 'talkapp/home.html')
