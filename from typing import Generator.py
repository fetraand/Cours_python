"""
Un générateur est une fonction Python spéciale qui utilise le mot-clé yield au lieu de return. 
Contrairement à une fonction classique qui s'arrête définitivement après un return,
un générateur suspend son exécution, renvoie sa valeur, et "se souvient" de son état exact pour reprendre là où il s'est arrêté lors du prochain appel.

Cela permet de créer des flux de données infinis ou de traiter d'immenses structures élément par élément, sans jamais tout charger en mémoire RAM d'un coup.
"""
from typing import Generator

def compteur_simple() -> Generator[int, None, None]:
    compte = 0
    while True:
        yield compte
        compte += 1

mon_flux = compteur_simple()
print(next(mon_flux))  # Affiche: 0
print(next(mon_flux))  # Affiche: 1
