from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import urllib
import urllib.request
import urllib3
import json
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
# Create your views here.

GOOGLE_RECAPTCIA_REQUIRED = True

def homepage(request):
    return render(request, "homepage.html")

def boardHandler(request, board_ID):
    try:
        currentBoard = board.objects.get(board_ID=board_ID)
    except board.DoesNotExist:
        return HttpResponse("404")
    Posts = Post.objects.filter(Post_Board=currentBoard).order_by("-Post_ID")
    return render(request, "board.html", {"boardName":currentBoard.board_name,
    "boardDesc":currentBoard.board_desc,
    "boardPic":currentBoard.board_picture,
    "boardID":currentBoard.board_ID,
    "Posts":Posts,
    })

def postingHandler(request, board_ID):
    if request.method == "POST":
        if GOOGLE_RECAPTCIA_REQUIRED == False:
            try:
                currentBoard = board.objects.get(board_ID=board_ID)
            except board.DoesNotExist:
                return HttpResponse("Error")
            Text = request.POST["text"]
            File = request.FILES["File"]
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
                OwO = Post(Post_Text=Text, Post_IP=ip, Post_Photo=File, Post_Board=currentBoard)
                OwO.save()
                return HttpResponseRedirect("/"+board_ID)
        else:
            recaptcha_response = request.POST['g-recaptcha-response']
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            req = requests.post(url, data=values)
            result_json = req.json()
            ''' End reCAPTCHA validation '''
            print(result_json)
            if result_json['success']:
                try:
                    currentBoard = board.objects.get(board_ID=board_ID)
                except board.DoesNotExist:
                    return HttpResponse("Error")
                Text = request.POST["text"]
                File = request.FILES["File"]
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                    OwO = Post(Post_Text=Text, Post_IP=ip, Post_Photo=File, Post_Board=currentBoard)
                    OwO.save()
                    return HttpResponseRedirect("/"+board_ID)
            else:
                return HttpResponse("Error")
    else:
        try:
            currentBoard = board.objects.get(board_ID=board_ID)
        except board.DoesNotExist:
            return HttpResponse("404")
        return render(request, "posting.html", {"name":currentBoard.board_name})

def ruleBook(request):
    return HttpResponse("lol finish me")
