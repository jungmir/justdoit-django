# board/models.py
from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(
        "comment.Comment", related_name="boards", blank=True
    )

    def __str__(self):
        return f"Board(id={self.pk}, '{self.title}')"
