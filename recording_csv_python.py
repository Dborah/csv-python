import csv

with open('recording.csv', mode='w') as csv_file:
    csv_file = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_file.writerow(['Name', 'Age', 'Occupation'])
    csv_file.writerow(['Deborah', '26', 'System Analyst'])
    csv_file.writerow(['Carla', '20', 'Data Scientist'])

