<div align="center">
  <h1>
    Trabajo Integrador Final
  </h1>
</div>

**Proyecto de la materia Desarrollo de Sistemas Orientado a Objetos**

Este archivo explica sus _componentes_ y el _modo de uso_.

## Componentes

- ### Archivo principal
1. main.py
> Compuesto de las opciones del menú, quien conecta con el archivo de las mismas.

- ### Carpeta ~ Funciones
2. opciones.py
> Compuesto por las clases: _BaseDeDatos_, _Coleccion_ y _Documento_.

3. csv.py
> Compuesto por el objeto _Archivo_, con este es que se realiza la segunda acción del menú.

- ### Carpeta ~ Registros
Está compuesto por los archivos
1. datos_personales.csv
> Archivo original del TP.

2. prueba_corta.csv
3. prueba_larga.csv
> Otros archivos de pruebas y ejemplos.

## Modo de Uso

El programa se inicializa en el archivo _main.py_, de ahí saltará un menú de opciones:
```bash
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
```
Según la opción seleccionada, la acción a realizar (desde la 2 a la 5 siempre hay que aclarar la colección).

En la segunda opción se puede elegir los datos de la _Carpeta ~ Registros_, las rutas de acceso son:
```bash
./Registros/datos_personales.csv
./Registros/prueba_corta.csv
./Registros/prueba_larga.csv
```
Para cualquier otro archivo que se encuentre fuera de la carpeta hay que poner la ruta.