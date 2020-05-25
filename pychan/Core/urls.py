from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("board/<str:board_ID>", views.boardHandler, name="boardHandler"),
]
