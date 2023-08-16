import time
import os
import re # Módulo de expresiones regulares

            ##### EJEMPLO DE USO DE RE #####
# Si en un archivo de XML tenemos el siguiente fragmento:
# <senal nombre="Prueba 1" t="5" A="4">
# Y tenemos la siguiente expresión regular:
# nombre_match = re.search(r'nombre="([^"]+)"', linea)
# Se busca un coincidencia donde la palabra 'nombre='
#  este seguida por un valor entre comillas dobles.
#   La parte de '([^"]+)' captura cualquier carácter que no
#    sea una comilla doble.

# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
# Definición de la clase Lista
class Lista:
    def __init__(self):
        self.cabeza = None
        
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente
            
# Definición de la clase Señal
class Senal:
    def __init__(self, nombre, t, A):
        self.nombre = nombre
        self.t = t
        self.A = A
        self.datos = Lista()
        
    def __str__(self):
        return f"Señal({self.nombre}, t={self.t}, A={self.A})"

    def agregar_dato(self, t, A, valor):
        self.datos.agregar((t, A, valor))
        

class SistemaAudio:
    
    def __init__(self):
        self.senales = Lista()

    def mostrar_menu(self):
        while True:
            print("\n--------- MENÚ PRINCIPAL ---------")
            print("1. Cargar archivo")
            print("2. Procesar archivo")
            print("3. Escribir archivo de salida")
            print("4. Mostrar datos del estudiante")
            print("5. Generar gráfica")
            print("6. Inicializar sistema")
            print("7. Salida")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.cargar_archivo()
            elif opcion == "2":
                self.procesar_archivo()
            elif opcion == "3":
                self.escribir_archivo_salida()
            elif opcion == "4":
                self.mostrar_datos_estudiante()
            #Aquí se pueden agregar las otras opciones (5) y (6)
            elif opcion == "7":
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...") #Pausa antes de borrar y mostrar el menú nuevamente

    def cargar_archivo(self):
        print("\n----------CARGAR ARCHIVO----------")
        ruta = input("Ingrese la ruta del archivo: ")
        
        # Se verifica si el archivo es de tipo .xml
        if not ruta.lower().endswith('.xml'):
            print("ERROR: Solo se aceptan archivos XML.")
            return
        
        if os.path.exists(ruta):
            print("Archivo cargado correctamente.")
            
            # Se lee y procesa el archivo XML
            with open(ruta, 'r') as archivo:
                for linea in archivo:
                    linea = linea.strip() # Se quitan los espacios al inicio y final de cada linea
            
                    if '<senal' in linea:
                        # EN DESARROLLO
                        pass
                    elif '<dato' in linea:
                        # EN DESARROLLO
                        pass
            
        else:
            print("Error: No se pudo encontrar el archivo.")
            #Podemos volver al menú principal aquí
            return

    def procesar_archivo(self):
        print("\nCalculando la matriz binaria...")
        time.sleep(10)  #Espera 10 segundos
        print("Realizando suma de tuplas...")
        time.sleep(10)  #Espera 10 segundos
        print("FELICIDADES")

    def escribir_archivo_salida(self):
        ruta = input("\nEscriba la ruta específica para el archivo de salida: ")
        #Aquí se escribira el archivo. Simularemos que se escribió.
        #Asegurar que la ruta es válida y que tengo permisos de escritura.
        print("Se escribió el archivo satisfactoriamente.")

    def mostrar_datos_estudiante(self):
        print("\nLuis Rodolfo Porras García")
        print("201901462")
        print("Introducción a la Programación y Computación 2 Sección 'A'")
        print("Ingeniería en Ciencias y Sistemas")
        print("4to Semestre")

if __name__ == "__main__":
    sistema = SistemaAudio()
    sistema.mostrar_menu()