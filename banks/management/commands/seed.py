from django.core.management.base import BaseCommand
import urllib.request, csv
import ssl
from banks.models import Banks

class Command(BaseCommand):
  def handle(self, *args, **options):
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://stat.fsc.gov.tw/FSC_OAS3_RESTORE/api/CSV_EXPORT?TableID=B14&OUTPUT_FILE=Y'
    webpage = urllib.request.urlopen(url) 
    data = csv.DictReader(webpage.read().decode('utf-8').splitlines()) 
    for row in data:
      head_code = row.get('\ufeff總機構代號')
      if head_code is not None:
        if len(head_code) < 3:
          head_code = head_code.zfill(3)

      Banks.objects.get_or_create(
        head_code = head_code,
        institution_code = row.get('機構代號'),
        institution =  row.get('機構名稱'),
        address = row.get('地址'),
        tel = row.get('電話'),
      )
    print("腳本執行完畢")