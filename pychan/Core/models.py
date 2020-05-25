from django.db import models

# Create your models here.

class board(models.Model):
    board_ID = models.CharField(max_length=5, primary_key=True)
    board_name = models.CharField(max_length=20)
    board_desc = models.TextField(max_length=1000)
    board_picture = models.ImageField(upload_to="board")
