'''
Opciones

Conección con el CSV
'''
from .csv import Archivo

class Documento:
    #Genera el id incremental
    autoinc = 0
    def __init__(self, contenido=None):
        self.id = Documento.autoinc
        Documento.autoinc += 1
        self.contenido = contenido if contenido is not None else {}
    
    def __str__(self):
        return f"{self.id} | {self.contenido}"

class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}
    
    #2. Importar CSV a colección
    def importar_csv(self, ruta):
        if not ruta:
            print(f"El archivo {ruta} no existe.")
            return
        try:
            with open(ruta, "rt") as file:
                schema = file.readline().replace("\n", "")
                csv = Archivo(schema)
                for line in file:
                    nuevo_doc = Documento(csv.convert(line.strip("\n"))) #El strip borra el \n que sale a lo último
                    self.aniadir_doc(nuevo_doc)
                print(f"CSV de la ruta '{ruta}' importado correctamente.")
        except Exception as e:
            print(f"Error al importar el archivo: {e}")
    
    def aniadir_doc(self, docu):
        self.documentos[docu.id] = docu
    
    #3. Consultar documento en colección
    def buscar_doc(self, id_docu):
        return self.documentos.get(id_docu, None)
    
    #4. Eliminar documento de colección
    def eliminar_doc(self, id_docu):
        if id_docu in self.documentos:
            del self.documentos[id_docu]
        else:
            print("Documento no encontrado.")
    
    #5. Listar todos los documentos en colección
    def listar_doc(self):
        return list(self.documentos.values())

class BaseDeDatos:
    def __init__(self):
        self.colecciones = {}
    
    #1. Crear colección
    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            print(f"La colección '{nombre_coleccion}' ya existe.")
        else:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
            print(f"Colección '{nombre_coleccion}' creada con éxito.")
    
    #Acción principal de la que deriva el funcionamiento las otras 4
    def obtener_coleccion(self, nombre_coleccion):
        return self.colecciones[nombre_coleccion]