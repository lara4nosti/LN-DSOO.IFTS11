'''
CSV

Lector del archivo
'''
class Archivo(object):
    def __init__(self, schemaStr, separator=","):
        if schemaStr is None:
            return print("El archivo está vacío.")
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
            return print("Los campos de la fila no concuerdan.")

#Pruebas para un archivo de las notificaciones de error
'''
class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

try:
    o = Archivo(2)
    d = o.convert(row)
    print(d)
except AttributeError:
    print("Parámetros incorrectos")
except SchemaError as e:
    print("Fallo algo en el schema:", e)
'''