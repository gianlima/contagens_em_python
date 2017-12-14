from csv import reader
from pprint import pprint

with open('/home/est/gls17/ce083/ce083/dados/crabs.csv') as csvfile:
    data = list(reader(csvfile, delimiter = ';'))

pprint(data)

print('Números de Azuis')

pprint(len([row[0] for row in data if row[0] == 'azul']))
    
    
