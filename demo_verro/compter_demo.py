# demo_compteur.py
import threading
from compter import Compteur


with open("stats.txt", "w") as f:
    f.write("0")

# Un premier compteur
compteur = Compteur()

# On lance NB threads qui vont tous incrémenter le compteur
def requete(no):
    c = Compteur()
    c.incrementer()

NB = 10
print(f"=== {NB} requêtes simultanées ===\n")

threads = [threading.Thread(target=requete, args=(i,)) for i in range(NB)]
for t in threads: t.start()
for t in threads: t.join()

c = Compteur()
print(f"Valeur attendue : {NB}")
print(f"Valeur obtenue  : {c.valeur()}")

if c.valeur() != NB:
    print(f"\n→ {NB - c.valeur()} incréments perdus — race condition.")
    print("  Modifiez compteur.py, puis relancez.")
else:
    print("\n✓  Tous les incréments comptés correctement.")