import csv

cwb_filename = '106060015.csv'
data = []
header = []
output = []
names = ['C0A880','C0F9A0','C0G640','C0R190','C0X260']

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

for ele in names:
    target_data = list(filter(lambda item: item['station_id'] == ele, data))
    small = 100
    big = 0
    no = 0
    for compo in target_data:
        n = float(compo['WDSD'])
        if n == -99.000 or n == -999.000: no = 1
        if n < small : small = n
        if n > big : big = n
    if no == 0:    output.append([ele,big - small])
    else:    output.append([ele,'none'])

print(output)
