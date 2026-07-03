# Module01/ex5 — Garden Security System (Encapsulation)

## Code

```python
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.age = age
        self._height = 0.0
        self.set_height(height)

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = height

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(-5.0)
    rose.show()
```

### Sortie attendue

```
=== Garden Security System ===
Plant created: Rose: 15.0cm, 10 days old

Rose: Error, height can't be negative
Rose: 15.0cm, 10 days old
```

## Explication du Code et des Concepts

Cet exercice introduit un pilier fondamental de la Programmation Orientée Objet (POO) : **l'Encapsulation**. Le but est de protéger l'état interne de l'objet (la plante) pour éviter qu'il ne soit corrompu par des données absurdes (comme une taille négative).

### La convention "Protected" (`_`)

En Python, préfixer un attribut par un simple tiret bas (ex: `self._height`) est une convention. Cela indique aux autres développeurs :

> « Attention, cet attribut est à usage interne, ne le modifiez pas directement depuis l'extérieur de la classe. »

C'est ce que l'exercice demande (au lieu du *name mangling* avec `__` qui rend l'accès techniquement plus difficile).

### Les Getters (`get_height`)

Puisque les attributs sont protégés (`_height`), on fournit des méthodes spécifiques, appelées **getters** (ou accesseurs), pour permettre au reste du programme de consulter ces valeurs en toute sécurité.

### Les Setters (`set_height`)

C'est ici que la magie de la sécurité opère. Au lieu de faire `rose._height = -5` (ce qui corromprait la donnée), le programmeur doit utiliser `rose.set_height(-5.0)`.

Le setter agit comme un agent de sécurité à l'entrée :
- il vérifie la valeur (`if height < 0`) ;
- si elle est valide, il l'enregistre ;
- sinon, il rejette la modification et affiche un message d'erreur, préservant ainsi l'intégrité de la plante.

### Validation à l'initialisation __init__ (`self.set_height(height)`)

Même lors de la création initiale de l'objet, les données fournies pourraient être mauvaises. C'est pourquoi le code vérifie également les valeurs dans le `__init__`. Si une valeur négative est passée à la création, la plante est créée avec une valeur par défaut (`0.0`) pour éviter un crash, et le message d'erreur est affiché.
