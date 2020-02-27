import csv

with open('resultado_da_consulta.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    print('Diárias e Passagens - Jan/Dez de 2018 do Governo do Minas')
    for row in csv_reader:
        if line_count == 0:
            print(f'Nome das colunas são {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} gastou {row[5]} {row[3]}')
            line_count += 1
    print(f'Processou {line_count} linhas.')
