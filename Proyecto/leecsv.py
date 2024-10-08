# Limpiar pantalla
import os
os.system('cls')

from s2d import Str2Dic

# f = open("Proyecto\\registros.csv", "rt")
f = open("Proyecto/registros.csv", "rt")
schema = f.readline().replace("\n", "")
parser = Str2Dic(schema)
row1 = f.readline().replace("\n", "")
row2 = f.readline().replace("\n", "")
print(parser.convert(row1))
print(parser.convert(row2))
print(schema)
print(row1)
print(row2)

