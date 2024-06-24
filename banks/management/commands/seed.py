from django.core.management.base import BaseCommand
import urllib.request, csv
import ssl
from banks.models import Banks, Branches

class Command(BaseCommand):
  def handle(self, *args, **options):
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://stat.fsc.gov.tw/FSC_OAS3_RESTORE/api/CSV_EXPORT?TableID=B14&OUTPUT_FILE=Y'
    webpage = urllib.request.urlopen(url) 
    data = csv.DictReader(webpage.read().decode('utf-8').splitlines()) 

    def get_head_and_branch(branch):
      match branch:
        case _ if '銀行' in branch:
            head = f'{branch.split("銀行")[0]}銀行'
            branch = branch.split("銀行")[1]
        case _ if '代表人辦事處' in branch:
            head = f'{branch.split("代表人辦事處")[0]}代表人辦事處'
            branch = branch.split("代表人辦事處")[1]
        case _ if '信用合作社' in branch:
            head = f'{branch.split("信用合作社")[0]}信用合作社'
            branch = branch.split("信用合作社")[1]
        case _:
            head = None
            branch = branch
      return head, branch

    for row in data:
      head_code = row.get('\ufeff總機構代號')
      if head_code is not None:
        if len(head_code) < 3:
          head_code = head_code.zfill(3)

      branch = row.get('機構名稱')
      head, branch = get_head_and_branch(branch)

      if head:
        head = head.replace('有限責任','').replace('保證責任','')
      if head is None:
        continue

      if branch:
        branch = branch.replace('股份有限公司','').replace('有限公司','')
        if branch.strip() == '':
          continue
      
      bank, created = Banks.objects.get_or_create(
        bank_code = head_code,
        defaults={
          'bank': head
        }
      )

      Branches.objects.get_or_create(
        branch_code = row.get('機構代號'),
        defaults={
        'head_code': bank,
        'branch': branch,
        'address': row.get('地址'),
        'tel': row.get('電話'),
        }
      )
    print("腳本執行完畢")