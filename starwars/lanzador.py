from clases.Starwars import *
from clases.Comprador import *
from clases.Vendedor import *
from clases.Holocron import *
from clases.Servidor import *


def menu():
    while True:
        print("----- Menú Principal -----")
        print("1. Ejercicio 1: Sistema de gestión de compra y venta de Holocrones")
        print("2. Ejercicio 2: Publicación y compra continua de anuncios")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            ejecutar_ejercicio_1()
        elif opcion == "2":
            ejecutar_ejercicio_2()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Introduce un número del 1 al 3.\n")


def ejecutar_ejercicio_1():
    print("Ejecutando el Ejercicio 1...")
    starwars = Starwars(31000)

    executor = ThreadPoolExecutor(max_workers=2)

    # Programamos y ejecutamos las tareas de forma concurrente en un bucle while
    executor.submit(starwars.comprar)
    executor.submit(starwars.vender)

    # Configuramos la gráfica en modo interactivo
    plt.ion()

    while True:
        # Graficar los valores a lo largo del tiempo
        plt.plot(starwars.time_values, starwars.dinero_values)
        plt.xlabel('Tiempo')
        plt.ylabel('Dinero restante')
        plt.title('Cambio del dinero restante')
        plt.grid(True)
        plt.pause(0.1)
        plt.clf()  # Limpiar la gráfica antes de la siguiente actualización



def ejecutar_ejercicio_2():
    print("Ejecutando el Ejercicio 2...")
    # Crear instancias del servidor, vendedores y compradores
    servidor = Servidor(capacidad_tablon=5)

    vendedores = [Vendedor(nombre=f"Vendedor{i}") for i in range(1, 6)]
    compradores = [Comprador(nombre=f"Comprador{i}", max_nivel_poder=random.randint(1, 3)) for i in range(1, 6)]

    # Crear hilos para publicar anuncios y realizar compras
    hilo_publicar = Thread(target=publicar_anuncios, args=(servidor, vendedores))
    hilo_comprar = Thread(target=realizar_compras, args=(servidor, compradores))

    # Iniciar los hilos
    hilo_publicar.start()
    hilo_comprar.start()

    # Esperar a que los hilos terminen (esto no sucederá en este caso ya que son bucles infinitos)
    hilo_publicar.join()
    hilo_comprar.join()