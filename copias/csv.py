# Limpiar pantalla
import os
os.system('cls')

schema = "Nombre,Apellido,Edad,DNI"
row = "Lara,Nosti,21,45.236.681"

class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Documento:
    #Genera el id icremental con cada documento que se le agregue
    autoinc = 0
    def __init__(self, contenido=None):
        self.id = Documento.autoinc
        Documento.autoinc += 1
        self.contenido = contenido if contenido is not None else {}
    
    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor
    
    def __str__(self):
        return f"Documento {self.id}, contenido: {self.contenido}"

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
    o = Archivo(2)
    d = o.convert(row)
    print(d)
except AttributeError:
    print("Parámetros incorrectos")
except SchemaError as e:
    print("Fallo algo en el schema:", e)


o = Archivo(schema)
print(o.schema)

d = o.convert(row)
print(d["DNI"])

# Otra cosa
o.tmp = "Jose"
o.PrintTmp()