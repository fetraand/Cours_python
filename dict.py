inventaire = {}
inventaire["épée"] = 3
print(inventaire)  # {'épée': 3}

inventaire["potion"] = 5
print(inventaire)  # {'épée': 3, 'potion': 5}

inventaire["épée"] = 10   # la clé existe déjà -> on écrase l'ancienne valeur
print(inventaire)  # {'épée': 10, 'potion': 5}
