from django.db import models

class Writing(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    inittime = models.DateTimeField(auto_now=True)

    writer = models.CharField(max_length=200, blank=True)

    class Board(models.TextChoices):
        AIRPLANE = 'airplane'
        CAR = 'car'

    board = models.CharField(
        max_length=10,
        choices=Board.choices,
        default=Board.AIRPLANE,
    )
