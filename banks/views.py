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
  branches = Branches.objects.all()
  branch_list = []
  for branch in branches:
    branch_list.append({
      'code':branch.branch_code,
      'title':branch.branch,
      'address':branch.address,
      'tel':branch.tel,
      'bank_code': branch.head_code.bank_code
    })
  return render(request, "banks/index.html", {'banks':banks, 'bank_list':bank_list, 'branch_list':branch_list})

