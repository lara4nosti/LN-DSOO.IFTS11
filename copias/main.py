'''
Interfaz

Conección con las Opciones
'''
from Funciones.opciones import BaseDeDatos
db = BaseDeDatos()

# Limpiar pantalla
import os

def mostrar_menu():
    os.system('cls')
    print("\n--- Base de Datos Documental ---")
    print("1. Crear colección")
    print("2. Importar CSV a colección")
    print("3. Consultar documento en colección")
    print("4. Eliminar documento de colección")
    print("5. Listar todos los documentos en colección")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            os.system('cls')
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            db.crear_coleccion(nombre_coleccion)
            print(f"Colección '{nombre_coleccion}' creada.")
            input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "2":
            os.system('cls')
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            collection = db.obtener_coleccion(nombre_coleccion)
            ruta_csv = input("Ingrese la ruta del archivo CSV: ")
            collection.importar_csv(nombre_coleccion, ruta_csv)
            input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "3":
            os.system('cls')
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            doc_id = int(input("Ingrese el ID del documento: "))
            coleccion = db.get_collection(nombre_coleccion)
            #collection = db.obtener_coleccion(nombre_coleccion)
            if coleccion:
                documento = coleccion.get_document(doc_id)
                if documento:
                    print("Documento encontrado:")
                    print(documento)
                else:
                    print("Documento no encontrado.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
            input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "4":
            os.system('cls')
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            doc_id = input("Ingrese el ID del documento a eliminar: ")
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                coleccion.delete_document(doc_id)
            input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "5":
            os.system('cls')
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.get_collection(nombre_coleccion)
            if coleccion:
                documentos = coleccion.list_documents()
                if documentos:
                    print("\n--- Lista de Documentos ---")
                    for doc in documentos:
                        print(doc)
                        print("-----------")
                else:
                    print("No hay documentos en la colección.")
            input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "6":
            os.system('cls')
            print("Saliendo del programa.")
            break
        
        else:
            os.system('cls')
            print("Opción no válida. Intente nuevamente.")
            input("\n-Presione Enter para volver al menú-")

if __name__ == "__main__":
    main()