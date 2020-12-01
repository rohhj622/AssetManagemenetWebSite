from django.db import models
from django.utils.timezone import now

# Create your models here.
class Asset(models.Model):
    a_id = models.AutoField(primary_key=True)
    m_id = models.CharField(max_length=12, null=False)
    a_saving = models.IntegerField(null=False)
    a_deposit = models.IntegerField(null=False)
    a_stock = models.IntegerField(null=False)
    a_fund = models.IntegerField(null=False)
    a_datetime = models.DateField(default=now, null=False)

class LovedTable(models.Model):
    l_idx = models.AutoField(primary_key=True)
    l_love = models.CharField(max_length=12, null=False)
    l_loved = models.CharField(max_length=12, null=False)
