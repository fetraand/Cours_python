class Batiment:
    nombre_de_Batiment = 0
    def __init__(self, name, taille, couleur) -> None:
        Batiment.nombre_de_Batiment += 1
        self.name = name
        self.taille = taille
        self.couleur = couleur
    def afficher(self):  
        print(f"{self.name} est {self.taille} avec une couleur {self.couleur}")


if __name__ == "__main__":
    bungalow = Batiment("Hotel", "Grand", "Blanc")
    print(f"Nombre de Batiment initier: {Batiment.nombre_de_Batiment}")


    """Il y a deux facons pour appeller la methode "afficher" """
    # 1. Syntaxe classique (la plus utilisée et intuitive)
    # Python comprend automatiquement que "bungalow" est l'objet passé en paramètre (self).
    bungalow.afficher()

    # 2. Syntaxe explicite (équivalent exact de ce que Python fait en arrière-plan)
    # On passe l'objet directement en argument à la méthode de la classe.
    Batiment.afficher(bungalow)
