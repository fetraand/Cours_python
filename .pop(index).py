"""
.pop(index) est une méthode de list qui fait deux choses en une seule opération :
elle retire l'élément à la position index de la liste et le retourne (te le renvoie), pour que tu puisses l'utiliser.
"""

liste = ["a", "b", "c", "d"]

element = liste.pop(1)
print(element)  # "b"          -> l'élément retiré
print(liste)    # ["a", "c", "d"]  -> la liste modifiée, sans "b"

"""
Points clés :

Sans argument, .pop() retire et retourne le dernier élément par défaut : liste.pop() équivaut à liste.pop(-1).
Contrairement à l'indexation simple liste[1] (qui lit sans modifier), .pop(1) modifie la liste en place (elle rétrécit de 1 élément).
Si l'index n'existe pas, ça lève une IndexError.

Dans ton consume_event(), events.pop(index) sert exactement à ça : retirer un élément aléatoire de la liste et le récupérer pour le yield immédiatement après, en une seule ligne.

"""
