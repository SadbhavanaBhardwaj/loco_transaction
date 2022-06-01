from django.db import models

# Create your models here.
class Transaction(models.Model):
    amount = models.FloatField()
    type  = models.CharField(max_length=25)
    parent_id = models.ForeignKey(to='self', on_delete=models.CASCADE)

    