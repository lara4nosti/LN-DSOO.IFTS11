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
            input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "2":
            os.system('cls')
            try: #Prueba para prevenir errores
                nombre_coleccion = input("Ingrese el nombre de la colección: ")
                collection = db.obtener_coleccion(nombre_coleccion)
                ruta_csv = input("Ingrese la ruta del archivo CSV: ")
                collection.importar_csv(ruta_csv)
                input("\n-Presione Enter para volver al menú-")
            except Exception as e: #Principalmente planeado para errores con el nombre de la colección
                print(f"Error al igresar el nombre de la colección: {e}")
                input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "3":
            os.system('cls')
            try: #Prueba para prevenir errores
                nombre_coleccion = input("Ingrese el nombre de la colección: ")
                collection = db.obtener_coleccion(nombre_coleccion)
                doc_id = int(input("Ingrese el ID del documento: "))
                if collection:
                    documento = collection.buscar_doc(doc_id)
                    if documento:
                        print("Documento encontrado:")
                        print(documento)
                    else:
                        print("Documento no encontrado.")
                else:
                    print(f"Colección '{nombre_coleccion}' no encontrada.")
                input("\n-Presione Enter para volver al menú-")
            except Exception as e: #Principalmente planeado para errores con el nombre de la colección
                print(f"Error al igresar el nombre de la colección: {e}")
                input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "4":
            try: #Prueba para prevenir errores
                os.system('cls')
                nombre_coleccion = input("Ingrese el nombre de la colección: ")
                collection = db.obtener_coleccion(nombre_coleccion)
                doc_id = int(input("Ingrese el ID del documento a eliminar: "))
                if collection:
                    collection.eliminar_doc(doc_id)
                input("\n-Presione Enter para volver al menú-")
            except Exception as e: #Principalmente planeado para errores con el nombre de la colección
                print(f"Error al igresar el nombre de la colección: {e}")
                input("\n-Presione Enter para volver al menú-")
        
        elif opcion == "5":
            try: #Prueba para prevenir errores
                os.system('cls')
                nombre_coleccion = input("Ingrese el nombre de la colección: ")
                collection = db.obtener_coleccion(nombre_coleccion)
                if collection:
                    documentos = collection.listar_doc()
                    if documentos:
                        print("\n--- Lista de Documentos ---")
                        for doc in documentos:
                            print(doc)
                            print("-----------")
                    else:
                        print("No hay documentos en la colección.")
                input("\n-Presione Enter para volver al menú-")
            except Exception as e: #Principalmente planeado para errores con el nombre de la colección
                print(f"Error al igresar el nombre de la colección: {e}")
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