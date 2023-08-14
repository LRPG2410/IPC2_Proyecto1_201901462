import time
import os

class SistemaAudio:
    
    def limpiar_consola(self): # Buscar otra alternativa por que no me funciona bien
        sistema = os.name
        if sistema == 'posix':
            os.system('clear')
        elif sistema == 'nt':  # Windows
            os.system('cls')

    def mostrar_menu(self):
        while True:
            self.limpiar_consola()
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
            # Aquí se pueden agregar las otras opciones (5) y (6)
            elif opcion == "7":
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...")  # Pausa antes de borrar y mostrar el menú nuevamente

    def cargar_archivo(self):
        print("\n----------CARGAR ARCHIVO----------")
        ruta = input("Ingrese la ruta del archivo: ")
        if os.path.exists(ruta):
            print("Archivo cargado correctamente.")
        else:
            print("Error: No se pudo encontrar el archivo.")
            # Podemos volver al menú principal aquí
            return

    def procesar_archivo(self):
        print("\nCalculando la matriz binaria...")
        time.sleep(10)  # Espera 10 segundos
        print("Realizando suma de tuplas...")
        time.sleep(10)  # Espera 10 segundos
        print("FELICIDADES")

    def escribir_archivo_salida(self):
        ruta = input("\nEscriba la ruta específica para el archivo de salida: ")
        # Aquí se escribira el archivo. Simularemos que se escribió.
        # Asegurar que la ruta es válida y que tengo permisos de escritura.
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