# Limpiar pantalla
import os
os.system('cls')

'''
a = 1
b = 0
a / b
'''

class SchemaError(Exception):
    def __init__(self, msg):
        self.message = msg
        super().__init__(msg)

try:
    a = 5 / 0
except SchemaError:
    print("Tiró la exception Schema")
except ZeroDivisionError:
    print("Tiró la exception Division por 0")

try:
    raise SchemaError("Pepito")
except SchemaError:
    print("Tiró la exception Schema")
except ZeroDivisionError:
    print("Tiró la exception Division por 0")

try:
    raise SchemaError("La cantidad de valores no corresponde con el schema")
except:
    print("Fallo por algo")

print(dir(SchemaError))