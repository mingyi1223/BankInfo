from django.db import models

class Banks (models.Model):
  bank_code = models.CharField(max_length=50)
  bank = models.CharField(max_length=50, null=True)

class Institutions (models.Model):
  head_code = models.ForeignKey(Banks, on_delete=models.CASCADE)
  institution_code = models.CharField(max_length=50, null=True)
  institution =  models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  tel = models.CharField(max_length=20)