# Les Méthodes de Classe (`@classmethod`)

## Code

```python
class Voiture:
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=180000)


lambo = Voiture.lamborghini()
porsche = Voiture.porsche()
print(porsche.prix)
```

### Sortie attendue

```
180000
```

## Explication du Code et des Concepts

Cet exemple introduit les **méthodes de classe** (`@classmethod`), un outil très utile pour créer des **constructeurs alternatifs**.

### Le décorateur `@classmethod`

Une méthode normale reçoit `self` (l'instance) en premier paramètre. Une méthode de classe reçoit `cls` (la classe elle-même) à la place, grâce au décorateur `@classmethod` placé juste au-dessus de la définition.

```python
@classmethod
def lamborghini(cls):
    ...
```

Cela veut dire que la méthode n'a pas besoin qu'un objet existe déjà pour être appelée : on peut l'appeler directement sur la classe, comme `Voiture.lamborghini()`.

### `cls` vs `self`

- `self` représente une **instance particulière** de la classe (un objet déjà créé).
- `cls` représente **la classe elle-même** (le "moule" qui sert à fabriquer des objets).

Utiliser `cls(...)` à l'intérieur de la méthode revient à appeler `Voiture(...)`, donc à créer une nouvelle instance. L'avantage d'écrire `cls` plutôt que `Voiture` en dur, c'est que si la classe est héritée plus tard, `cls` pointera automatiquement vers la bonne sous-classe.

### Le rôle de constructeur alternatif

Ici, `lamborghini()` et `porsche()` sont des **raccourcis de création** : au lieu d'écrire à chaque fois

```python
lambo = Voiture("Lamborghini", 250, 200000)
```

on peut simplement écrire :

```python
lambo = Voiture.lamborghini()
```

Cela rend le code plus lisible et évite de répéter des valeurs "magiques" (marque, vitesse, prix) à plusieurs endroits du programme. Toute la logique de construction d'une Lamborghini ou d'une Porsche est centralisée dans une seule méthode, facile à maintenir.

### Ce qui se passe à l'exécution

1. `Voiture.lamborghini()` appelle la méthode de classe, qui exécute `cls(marque="Lamborghini", vitesse=250, prix=200000)`, c'est-à-dire `Voiture(...)`. Cela déclenche `__init__` et retourne un nouvel objet `Voiture`.
2. Idem pour `Voiture.porsche()`.
3. `print(porsche.prix)` affiche l'attribut `prix` de l'objet `porsche`, soit `180000`.
