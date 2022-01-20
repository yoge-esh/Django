from django.db import models


class post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()

    def __str__(self):
        # return self.title[:50]
        return self.title
