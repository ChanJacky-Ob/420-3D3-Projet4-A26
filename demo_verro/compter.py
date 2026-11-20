# compteur.py — avec Singleton
import time
import threading

class Compteur:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            nouvelle = super().__new__(cls)
            nouvelle._initialiser()
            cls._instance = nouvelle     # assignation APRÈS l'init complète
        return cls._instance

    def _initialiser(self):
        self._verrou = threading.Lock()  # un seul verrou, partagé par tous les threads
        with open("stats.txt", "w") as f:
            f.write("0")
       

    def incrementer(self):
        with self._verrou:               # tous les threads attendent le même verrou
            with open("stats.txt", "r") as f:
                n = int(f.read().strip())
            time.sleep(0.05)
            with open("stats.txt", "w") as f:
                f.write(str(n + 1))

    def valeur(self):
        with open("stats.txt", "r") as f:
            return int(f.read().strip())