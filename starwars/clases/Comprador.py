from threading import Lock, Thread
import random
import time

class Comprador:
    def __init__(self, nombre, max_nivel_poder):
        self.nombre = nombre
        self.max_nivel_poder = max_nivel_poder

    def realizar_compra(self, servidor):
        holocron = servidor.buscar_holocron(self.max_nivel_poder)
        if holocron:
            servidor.realizar_venta(holocron, self)