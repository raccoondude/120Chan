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
    return render(request, "board.html")
