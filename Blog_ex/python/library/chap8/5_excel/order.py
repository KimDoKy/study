import openpyxl
wb = openpyxl.load_workbook('sample.xlsx', data_only=True)
ws = wb.get_active_sheet()

print('A1 -> A2 -> ... B1 -> B2의 순서로 값을 얻습니다. \n--------')

for row in ws.rows:
   for cell in row:
       print(cell.value)
       
print('\nA1 -> B1 -> A2 -> 의 순서로 값을 얻습니다. \n---------')

for column in ws.columns:
    for cell in column:
          print(cell.value)
