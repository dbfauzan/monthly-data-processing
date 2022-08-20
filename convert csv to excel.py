import pandas as pd
import glob
from openpyxl import Workbook
import csv

# read all file in PWD
listing = glob.glob("*.csv")
print(len(listing))

wb = Workbook()
ws = wb.active
for element in listing:
    file_csv = element[0:11] + '.csv'
    excel = element[0:11] + '.xlsx'
    with open(file_csv, 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save(excel)