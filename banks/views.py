from django.shortcuts import render
from .models import Banks, Branches

def index(request):
  banks = Banks.objects.all()
  return render(request, "banks/index.html", {'banks':banks})