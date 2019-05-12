
import csv
with open('data2.csv','w') as csvfile:
    fieldnames = ['id','name','age']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'id':'10001','name':'Mike','age':20})
    writer.writerow({'id': '10002', 'name': 'Jsp', 'age': 21})
    writer.writerow({'id': '10003', 'name': 'Bob', 'age': 22})












