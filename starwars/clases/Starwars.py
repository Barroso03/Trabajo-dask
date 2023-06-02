import matplotlib.pyplot as plt
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import random
import time


class Starwars:
    def __init__(self, dinerorestante):
        self.buffer = []
        self.capacidadmaxima = 100000
        self.valormoneda = random.randrange(0, 1000)
        self.dinerorestante = dinerorestante
        self.lock = Lock()
        self.time_values = []
        self.dinero_values = []

    def comprar(self):
        while True:
            with self.lock:
                if self.dinerorestante < self.valormoneda:
                    print("No tienes dinero suficiente")
                elif self.dinerorestante <= 30000:
                    print("Tu dinero ha bajado de 30000")
                else:
                    print("Comprando moneda")
                    self.dinerorestante -= self.valormoneda
                    self.buffer.append(self.valormoneda)
                    print("Dinero restante:", self.dinerorestante)
                    self.time_values.append(time.time())
                    self.dinero_values.append(self.dinerorestante)
            time.sleep(2)

    def vender(self):
        while True:
            with self.lock:
                if not self.buffer:
                    print("No tienes monedas para vender")
                else:
                    print("Vendiendo moneda")
                    moneda = self.buffer.pop()
                    self.dinerorestante += moneda
                    print("Dinero restante:", self.dinerorestante)
                    self.time_values.append(time.time())
                    self.dinero_values.append(self.dinerorestante)
            time.sleep(2)




