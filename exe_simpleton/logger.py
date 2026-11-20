import sqlite3, datetime
import threading


class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            nouvelle = super().__new__(cls)
            nouvelle._initialiser()  # initialisation après la création de l'instance
            cls._instance = nouvelle
        return cls._instance

    def _initialiser(self):
        self.verrou = threading.Lock()  # un seul verrou, partagé par tous les threads
        self.connexion = sqlite3.connect("logs.db")
        self.connexion.execute(
            "CREATE TABLE IF NOT EXISTS logs (ts TEXT, message TEXT)"
        )
        self.connexion.commit()

    def log(self, message: str) -> None:
        ts = datetime.datetime.now().isoformat()
        self.connexion.execute("INSERT INTO logs VALUES (?, ?)", (ts, message))
        self.connexion.commit()
        print(f"[{ts}] {message}")

    def tous_les_logs(self) -> list[tuple]:
        return self.connexion.execute("SELECT * FROM logs").fetchall()