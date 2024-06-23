from django.db import models

class Banks (models.Model):
  head_code = models.CharField(max_length=50, null=True)
  institution_code = models.CharField(max_length=50, null=True)
  institution =  models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  tel = models.CharField(max_length=20)