import csv

with open('recording2.csv', mode='w') as csv_file:
    fieldnames = ['Name', 'Age', 'Occupation']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'Deborah', 'Age': '26', 'Occupation': 'System Analyst'})
    writer.writerow({'Name': 'Carla', 'Age': '20', 'Occupation': 'Data Scientist'})


