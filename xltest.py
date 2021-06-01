import xlwings as xw
from datetime import datetime


wb = xw.Book("C:\\Users\\HJ\Desktop\\문서\\test\\cdn\\지출결의서_CDN_03월 요금.xls")
sht1 = wb.sheets[0]

time = datetime.today()

time_ymd = time.strftime('%Y%m%d') #년-월-일
time_m = time.strftime('%m') #월

sht1.range('F13').value = 'CDN 서비스 ' +time_m+'월 요금'
sht1.range('F13').value

file_name='C:\\Users\\HJ\\Desktop\\문서\\지출결의서\\CDN\\지출결의서_CDN_' +time_m+'월_요금_'+time_ymd+'.xls'
wb.save(file_name)

wb=xw.Book(file_name)
wb.sheets[0].api.PrintOut()
wb.close()
