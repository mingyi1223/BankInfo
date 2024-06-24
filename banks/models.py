from django.db import models

class Banks (models.Model):
  bank_code = models.CharField(max_length=50)
  bank = models.CharField(max_length=50, null=True)

class Branches (models.Model):
  head_code = models.ForeignKey(Banks, on_delete=models.CASCADE)
  branch_code = models.CharField(max_length=50, null=True)
  branch =  models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  tel = models.CharField(max_length=20)