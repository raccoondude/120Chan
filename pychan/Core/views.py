from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def boardHandler(request, board_ID):
    try:
        currentBoard = board.objects.get(board_ID=board_ID)
    except board.DoesNotExist:
        return HttpResponse("404")
    Posts = Post.objects.filter(Post_Board=currentBoard)
    return render(request, "board.html", {"boardName":currentBoard.board_name,
    "boardDesc":currentBoard.board_desc,
    "boardPic":currentBoard.board_picture,
    "Posts":Posts,
    })
