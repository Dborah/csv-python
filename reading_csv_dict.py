import csv

with open('resultado_da_consulta.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'As colunas são {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row["Credor"]} gastou {row["Valor"]} {row["Descrição"]}')
            line_count += 1
    print(f'Processou {line_count} linhas.')

