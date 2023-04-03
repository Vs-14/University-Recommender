from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    rank = models.IntegerField()
    gre = models.IntegerField()
    toefl = models.IntegerField()
    cgpa = models.DecimalField(max_digits=4,decimal_places=2)