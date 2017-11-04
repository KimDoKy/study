import csv

with open('sample.csv', mode='r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row)
