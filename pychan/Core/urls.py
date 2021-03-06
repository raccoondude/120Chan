from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<str:board_ID>/", views.boardHandler, name="boardHandler"),
    path("<str:board_ID>/post/", views.postingHandler, name="postingHandler"),
]
