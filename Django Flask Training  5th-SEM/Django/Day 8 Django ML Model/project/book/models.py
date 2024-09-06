from django.db import models

# Create your models here.

class BookD(models.Model):
    bname = models.CharField(max_length=30)
    bprice = models.IntegerField()

    def __str__(self) -> str:
        return self.bname