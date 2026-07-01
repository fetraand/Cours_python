# 🎓 Cours Python : Maîtriser `super()`

La fonction `super()` est un outil indispensable de la programmation orientée objet (POO) en Python. Elle permet à une classe enfant d'accéder aux méthodes et aux attributs de sa classe parente sans nommer explicitement cette dernière.

---

## 💡 Pourquoi utiliser `super()` ?

Sans `super()`, si vous modifiez le nom de la classe parente, vous devez changer ce nom partout dans vos classes enfants. `super()` rend votre code :
* **Flexible** (facile à modifier)
* **Maintenant** (évite la duplication de code)
* **Évolutif** (compatible avec les architectures complexes)

Sa fonction principale est d'**étendre** le comportement d'une méthode parente au lieu de la remplacer complètement.

---

## 🛠️ La syntaxe de base : Le constructeur `__init__`

L'usage le plus fréquent de `super()` se trouve dans le constructeur `__init__`. Il permet d'hériter des attributs de la classe parente tout en ajoutant de nouveaux attributs spécifiques à la classe enfant.

```python
class Batiment:
    def __init__(self, name, taille):
        self.name = name
        self.taille = taille

# Maison hérite de Batiment
class Maison(Batiment):
    def __init__(self, name, taille, nb_pieces):
        # 1. On appelle le constructeur du parent pour initialiser name et taille
        super().__init__(name, taille)
        
        # 2. On ajoute l'attribut spécifique à la classe Maison
        self.nb_pieces = nb_pieces

# Test
ma_maison = Maison("Villa", "Grand", 5)
print(ma_maison.name)       # Sortie : Villa (Vient de Batiment)
print(ma_maison.nb_pieces)  # Sortie : 5     (Vient de Maison)
```

---

## 🔄 Étendre une méthode classique

`super()` ne sert pas que pour le constructeur `__init__`. Vous pouvez l'utiliser dans n'importe quelle autre méthode pour enrichir un comportement existant.

```python
class Batiment:
    def afficher(self):
        print(f"C'est un bâtiment nommé {self.name}.")

class Hotel(Batiment):
    def afficher(self):
        # On exécute le code de la méthode afficher() du parent
        super().afficher()
        # On ajoute un comportement spécifique à l'Hotel
        print("Bienvenue à la réception !")

# Test
mon_hotel = Hotel("Plaza", "Très Grand")
mon_hotel.afficher()
# Sortie :
# C'est un bâtiment nommé Plaza.
# Bienvenue à la réception !
```

---

## ⚠️ Le piège de l'héritage multiple : Le MRO

Quand une classe hérite de plusieurs parents, Python utilise un algorithme appelé **MRO (Method Resolution Order)**. C'est l'ordre linéaire dans lequel Python cherche les méthodes dans la hiérarchie.

```python
class A:
    def action(self):
        print("Action de A")

class B(A):
    def action(self):
        print("Action de B")
        super().action()

class C(A):
    def action(self):
        print("Action de C")
        super().action()

class D(B, C):
    def action(self):
        print("Action de D")
        super().action()

# Test
d = D()
d.action()
```

### Ordre d'exécution obtenu :
1. *Action de D*
2. *Action de B*
3. *Action de C* *(Appelé par le `super()` de B !)*
4. *Action de A*

💡 **Astuce :** Vous pouvez inspecter l'ordre exact choisi par Python en affichant la propriété `__mro__` de la classe :
```python
print(D.__mro__)
# Target : (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

---

## 🎯 Ce qu'il faut retenir

* **Syntaxe moderne** : En Python 3, écrivez simplement `super()`. L'ancienne syntaxe `super(ClasseEnfant, self)` n'est plus nécessaire.
* **Héritage propre** : Ne dupliquez jamais le code d'initialisation des parents.
* **Cycle unique** : En héritage multiple, `super()` garantit que chaque classe parente n'est appelée qu'**une seule fois**.
