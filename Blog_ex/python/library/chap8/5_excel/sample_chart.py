import openpyxl
import random
from openpyxl.chart import Reference, Series, LineChart

wb = openpyxl.Workbook()
ws = wb.active

for i in range(10):
    ws.append([random.randint(1, 10)])

values = Reference(ws, min_row=1, min_col=1, max_row=10, max_col=1)
series = Series(values, title="Sample Chart")
chart = LineChart()
chart.append(series)
ws.add_chart(chart)

wb.save("sample_cahrt.xlsx")
