from django.shortcuts import render
from .models import Banks, Branches
from django.http import JsonResponse

def index(request):
  banks = Banks.objects.all()
  bank_list = []
  for bank in banks:
    bank_list.append({
      'code':bank.bank_code,
      'title':bank.bank
      })
  return render(request, "banks/index.html", {'banks':banks, 'bank_list':bank_list})

