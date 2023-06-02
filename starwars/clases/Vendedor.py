from threading import Lock, Thread
import random
import time

class Vendedor:
    def __init__(self, nombre):
        self.nombre = nombre

    def publicar_anuncio(self, holocron, servidor):
        servidor.agregar_anuncio(holocron, self)