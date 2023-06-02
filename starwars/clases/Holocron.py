from threading import Lock, Thread
import random
import time

class Holocron:
    def __init__(self, nivel_poder):
        self.nivel_poder = nivel_poder