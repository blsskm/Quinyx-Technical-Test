import pandas as pd
from datetime import datetime as dt
from openpyxl import Workbook, load_workbook

data = pd.read_excel('/Users/blasius/Desktop/Python/techtest/data.xlsx')
wb = Workbook()
ws = wb.active
ws.title = "Output"

x=0
y=1

def time(x):
    return data.loc[x, 'time']

time_1 = dt.strptime(time(x), "%Y-%m-%d %H:%M:%S")
time_2 = dt.strptime(time(y), "%Y-%m-%d %H:%M:%S") 

def sale(x):
    return data.loc[x, 'sales']

sale_sum = sale(x)

time_interval = time_2 - time_1
print (time_interval)




wb.save('Output.xlsx')

