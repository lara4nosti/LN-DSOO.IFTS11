'''
Opciones

Conección con las funciones
'''
#from nomPY import nomClase

# Limpiar pantalla
import os
os.system('cls')

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

class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}
    
    def aniadir_d(self, docu):
        self.documentos[docu.id] = docu
    
    def eliminar_d(self, id_docu):
        if id_docu in self.documentos:
            del self.documentos[id_docu]
    
    def buscar_d(self, id_docu):
        return self.documentos.get(id_docu, None)
    
    def __str__(self):
        return f"Colección {self.nombre}, con: {len(self.documentos)} documentos"

class BaseDeDatos:
    def __init__(self):
        self.colecciones = {}
    
    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
    
    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
    
    def obtener_coleccion(self, nombre_coleccion):
        return self.colecciones[nombre_coleccion]
    
    def __str__(self):
        return f"Base de datos documental con {len(self.colecciones)} colecciones"








db = BaseDeDatos()
c = Coleccion('muniecas')
m1 = Documento({'marca': 'Barbie', 'estetica': 'personalizable'})
m2 = Documento({'marca': 'Monster High', 'estetica': 'gótica'})
c.aniadir_d(m1)
c.aniadir_d(m2)
print(str(c))

munieca = c.buscar_d(1)
print(munieca.obtener_valor('marca'), munieca.obtener_valor('estetica'))
c.eliminar_d(munieca.id)
munieca = c.buscar_d(1)
if munieca is not None:
    print(munieca.obtener_valor('marca'), munieca.obtener_valor('estetica'))
else:
    print("La muñeca no existe más")