from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import random


class Starwars:
    def __init__(self,dinerorestante):
        self.buffer = []
        self.capacidadmaxima = 100000
        self.valormoneda = random.randrange(0,1000)
        self.dinerorestante=dinerorestante
        self.lock = Lock()

    def comprar(self):
        self.lock.acquire()
        while self.buffer <= self.capacidadmaxima:
            
            if self.dinerorestante>=self.valormoneda:
                if self.dinerorestante <= 30000:
                    print("Tu dinero ha bajado de 30000")
                print("Comprando moneda")
                self.dinerorestante=self.dinerorestante-self.valormoneda
                self.buffer.append(self.valormoneda)
                print("Dinero restante: ",self.dinerorestante)
                self.lock.release()
            else:
                print("No tienes dinero suficiente")
                break


    def vender(self):
        self.lock.acquire()
        while self.dinerorestante >= self.valormoneda:
            print("Vendiendo moneda")
            self.dinerorestante=self.dinerorestante +self.valormoneda
            print("Dinero restante: ",self.dinerorestante)
            self.lock.release()

if __name__ == '__main__':
    print('Creamos un pool  con 2 threads')
    starwars = Starwars(100000)

    executor = ThreadPoolExecutor(max_workers=1)

    # Programamos y ejecutamos 4 tareas de forma concurrente
    # Al solo existir 2 threads estas 2 tareas se ejecutarán primero
    executor.submit(starwars.comprar)
    executor.submit(starwars.vender)

   