from django.db import models
# Create your models here.


class Member(models.Model):
    m_id = models.CharField(max_length=12, primary_key=True, null=False)
    m_pw = models.CharField(max_length=12, null=False)
    m_name = models.CharField(max_length=24, null=False)
    m_sdrate = models.IntegerField(null=False)
    m_srate = models.IntegerField(null=False)
    m_frate = models.IntegerField(null=False)


class Asset(models.Model):
    a_id = models.IntegerField(primary_key=True, null=False)
    m_id = models.ForeignKey(Member, on_delete=models.CASCADE) #Member에서 m_id 삭제시,
    a_saving = models.IntegerField()
    a_deposit = models.IntegerField()
    a_stock = models.IntegerField()
    a_fund = models.IntegerField()
