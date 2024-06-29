from django.shortcuts import render, get_object_or_404
from .models import Banks, Branches

def index(request, bank_code=None, branch_code=None, bank_title=None, branch_title=None):
    banks = Banks.objects.all()
    bank_list = []
    for bank in banks:
        bank_list.append({
            'code': bank.bank_code,
            'title': bank.bank
        })

    branches = Branches.objects.all()
    branch_list = []
    for branch in branches:
        branch_list.append({
            'code': branch.branch_code,
            'title': branch.branch,
            'address': branch.address,
            'tel': branch.tel,
            'bank_code': branch.head_code.bank_code
        })

    selected_bank = None
    selected_branch = None

    if bank_code and branch_code:
        selected_bank = get_object_or_404(Banks, bank_code=bank_code)
        selected_branch = get_object_or_404(Branches, branch_code=branch_code, head_code=selected_bank)

    context = {
        'banks': banks,
        'bank_list': bank_list,
        'branch_list': branch_list,
        'selected_bank': selected_bank,
        'selected_branch': selected_branch
    }

    return render(request, "banks/index.html", context)


