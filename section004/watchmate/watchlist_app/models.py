from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)  # 映画の名称
    description = models.CharField(max_length=1000)  # 映画の説明文章
    active = models.BooleanField(default=True)  # 映画が公開されているかのフラグ

    def __str__(self):
        return self.name
