from tabulate import tabulate
from collections import Counter
import os

sides = 20
counter = Counter()

table_data = [['Dado 1','Dado 2','Dado 3','Suma']]

for dice1 in range(1,sides + 1):
    for dice2 in range(1,sides + 1):
        for dice3 in range(1,sides + 1):
            sum = dice1+dice2+dice3
            table_data.append([dice1,dice2,dice3,sum])
            counter[sum] +=1

sorted_sums = sorted(counter.items(),key=lambda x: x[1], reverse=True)

sum_table = [['Suma', 'Cantidad de Apariciones']] + sorted_sums


output_text = tabulate(table_data, headers="firstrow") + "\n\n"
output_text += "Frecuencia de sumas ordenada por apariciones:\n"
output_text += tabulate(sum_table, headers="firstrow")

ruta_archivo = os.path.abspath("archivo.txt")

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(output_text)
    print(f"Archivo guardado en: {ruta_archivo}")