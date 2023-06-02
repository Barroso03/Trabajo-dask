from threading import Lock, Thread
from clases.Holocron import Holocron
import random
import time


class Servidor:
    def __init__(self, capacidad_tablon):
        self.capacidad_tablon = capacidad_tablon
        self.tablon = []
        self.lock = Lock()

    def agregar_anuncio(self, holocron, vendedor):
        with self.lock:
            if len(self.tablon) < self.capacidad_tablon:
                anuncio = (holocron, vendedor)
                self.tablon.append(anuncio)
                print(f"Anuncio publicado: Holocron de nivel {holocron.nivel_poder} - Vendedor: {vendedor.nombre}")
            else:
                print("El tablón está completo. No se puede publicar el anuncio.")

    def buscar_holocron(self, max_nivel_poder):
        with self.lock:
            for anuncio in self.tablon:
                holocron, _ = anuncio
                if holocron.nivel_poder <= max_nivel_poder:
                    return holocron
            return None

    def realizar_venta(self, holocron, comprador):
        with self.lock:
            anuncio = None
            for a in self.tablon:
                h, v = a
                if h == holocron:
                    anuncio = a
                    break
            if anuncio:
                self.tablon.remove(anuncio)
                print(f"Venta realizada: Holocron de nivel {holocron.nivel_poder} - Comprador: {comprador.nombre}")
            else:
                print("El Holocron ya no está disponible.")
                
def publicar_anuncios(servidor, vendedores):
    while True:
        for vendedor in vendedores:
            holocron = Holocron(nivel_poder=random.randint(1, 3))
            vendedor.publicar_anuncio(holocron, servidor)
            time.sleep(random.uniform(0.5, 1.5))


def realizar_compras(servidor, compradores):
    while True:
        for comprador in compradores:
            comprador.realizar_compra(servidor)
            time.sleep(random.uniform(0.5, 1.5))


