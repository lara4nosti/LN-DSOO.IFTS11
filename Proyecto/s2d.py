# Limpiar pantalla
import os
os.system('cls')

schema = "Nombre;Apellido;Edad;DNI"
row = "Lara;Nosti;20;45.236.681"

class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Str2Dic(object):
    def __init__(self, schemaStr, separator=";"):
        if len(schema) == 0:
            raise SchemaError("El schema está vacío")
        self.schema = schemaStr.split(separator)
        self.separator = separator
    
    def convert(self, row):
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d = {}
            ''' Otra forma:
            while i < len(tmp):
                d[self.schema[i]] = tmp[i]
                i += 1
            '''
            while i < len(tmp):
                key = self.schema[i]
                val = tmp[i]
                d[key] = val
                i += 1
            return d
        else:
            raise SchemaError("Los campos de la fila no concuerdan con el schema")
    
    # Otra cosa
    def PrintTmp(self):
        print(self.tmp)

try:
    o = Str2Dic(2)
    d = o.convert(row)
    print(d)
except AttributeError:
    print("Parámetros incorrectos")
except SchemaError as e:
    print("Fallo algo en el schema:", e)


o = Str2Dic(schema)
print(o.schema)

d = o.convert(row)
print(d["DNI"])

# Otra cosa
o.tmp = "Jose"
o.PrintTmp()