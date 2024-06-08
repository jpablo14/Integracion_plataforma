# Integracion_plataforma
# capa_presentacion.py
class CapaPresentacion:
    def __init__(self):
        pass
    
    def mostrar_menu_principal(self):
        print("Bienvenido a Ferramas")
        print("1. Realizar una venta")
        print("2. Gestionar inventario")
        print("3. Generar reportes")
        print("4. Salir")

    def obtener_opcion(self):
        return input("Ingrese su opción: ")

# capa_negocios.py
class CapaNegocios:
    def __init__(self):
        pass
    
    def realizar_venta(self):
        pass
    
    def gestionar_inventario(self):
        pass
    
    def generar_reportes(self):
        pass

# capa_datos.py
class CapaDatos:
    def __init__(self):
        pass
    
    def cargar_inventario(self):
        pass
    
    def guardar_venta(self, venta):
        pass

# main.py
from capa_presentacion import CapaPresentacion
from capa_negocios import CapaNegocios
from capa_datos import CapaDatos

def main():
    capa_presentacion = CapaPresentacion()
    capa_negocios = CapaNegocios()
    capa_datos = CapaDatos()

    while True:
        capa_presentacion.mostrar_menu_principal()
        opcion = capa_presentacion.obtener_opcion()

        if opcion == '1':
            capa_negocios.realizar_venta()
        elif opcion == '2':
            capa_negocios.gestionar_inventario()
        elif opcion == '3':
            capa_negocios.generar_reportes()
        elif opcion == '4':
            print("Gracias por usar Ferramas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()

# capa_datos.py
class CapaDatos:
    def __init__(self):
        self.inventario = [
            {"id": 1, "nombre": "Martillo", "cantidad": 50, "precio_unitario": 10.99},
            {"id": 2, "nombre": "Destornillador", "cantidad": 100, "precio_unitario": 5.99},
            {"id": 3, "nombre": "Sierra", "cantidad": 30, "precio_unitario": 20.99},
            # Agrega más productos aquí si lo deseas
        ]

    def cargar_inventario(self):
        return self.inventario

# capa_negocios.py
from capa_datos import CapaDatos

class CapaNegocios:
    def __init__(self):
        self.capadatos = CapaDatos()

    def imprimir_inventario(self):
        inventario = self.capadatos.cargar_inventario()
        print("Inventario de Ferramas:")
        print("ID | Nombre           | Cantidad | Precio Unitario")
        print("-" * 45)
        for producto in inventario:
            print(f"{producto['id']:2} | {producto['nombre']:<16} | {producto['cantidad']:8} | ${producto['precio_unitario']:0.2f}")

# capa_presentacion.py
from capa_negocios import CapaNegocios

class CapaPresentacion:
    def __init__(self):
        self.capanegocios = CapaNegocios()

    def mostrar_menu_principal(self):
        print("Bienvenido a Ferramas")
        print("1. Realizar una venta")
        print("2. Ver inventario")
        print("3. Generar reportes")
        print("4. Salir")

    def obtener_opcion(self):
        return input("Ingrese su opción: ")

    def ejecutar_opcion(self, opcion):
        if opcion == '1':
            pass  # Aquí llamaremos a la función de realizar venta
        elif opcion == '2':
            self.capanegocios.imprimir_inventario()
        elif opcion == '3':
            pass  # Aquí llamaremos a la función de generar reportes
        elif opcion == '4':
            print("Gracias por usar Ferramas. ¡Hasta luego!")
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

