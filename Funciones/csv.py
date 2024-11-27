'''
CSV

Lector del archivo
'''
class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Archivo(object):
    def __init__(self, schemaStr, separator=","):
        if len(schema) == 0:
            raise SchemaError("El schema está vacío")
        self.schema = schemaStr.split(separator)
        self.separator = separator
    
    def convert(self, row):
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d = {}
            while i < len(tmp):
                key = self.schema[i]
                val = tmp[i]
                d[key] = val
                i += 1
            return d
        else:
            raise SchemaError("Los campos de la fila no concuerdan con el schema")

#Pruebas para un archivo de las notificaciones de error
'''
try:
    o = Archivo(2)
    d = o.convert(row)
    print(d)
except AttributeError:
    print("Parámetros incorrectos")
except SchemaError as e:
    print("Fallo algo en el schema:", e)
'''