# Les Classes Imbriquées (Nested Classes)

## Code

```python
class Voiture:
    class Moteur:
        def __init__(self, puissance, carburant):
            self.puissance = puissance
            self.carburant = carburant

        def demarrer(self):
            print(f"Le moteur {self.carburant} de {self.puissance}ch démarre...")

    def __init__(self, marque, puissance, carburant):
        self.marque = marque
        self.moteur = self.Moteur(puissance, carburant)

    def demarrer(self):
        print(f"{self.marque}: ", end="")
        self.moteur.demarrer()


lambo = Voiture("Lamborghini", 640, "essence")
lambo.demarrer()
print(lambo.moteur.puissance)
```

### Sortie attendue

```
Lamborghini: Le moteur essence de 640ch démarre...
640
```

## Explication du Code et des Concepts

Une **classe imbriquée** (nested class) est une classe définie **à l'intérieur** d'une autre classe. Elle sert à modéliser une relation de type *"fait partie de"* (composition) : ici, un `Moteur` n'a de sens que parce qu'il appartient à une `Voiture`.

### Définir une classe imbriquée

```python
class Voiture:
    class Moteur:
        def __init__(self, puissance, carburant):
            ...
```

`Moteur` est déclarée directement dans le corps de `Voiture`, au même niveau que les méthodes. C'est une classe à part entière, avec son propre `__init__` et ses propres méthodes.

### Comment l'instancier

Pour créer un objet `Moteur` depuis l'extérieur, il faut passer par `Voiture` :

```python
moteur = Voiture.Moteur(640, "essence")
```

Mais en général, on ne fait pas ça directement de l'extérieur. On instancie plutôt le `Moteur` **depuis l'intérieur** de `Voiture`, dans son `__init__` :

```python
def __init__(self, marque, puissance, carburant):
    self.marque = marque
    self.moteur = self.Moteur(puissance, carburant)
```

Ici, `self.Moteur` fonctionne aussi bien que `Voiture.Moteur`, car `self` a accès à tout ce que sa classe contient.

### Pourquoi utiliser une classe imbriquée plutôt que deux classes séparées ?

- **Regroupement logique** : `Moteur` n'a de sens que dans le contexte d'une `Voiture`. Le mettre à l'intérieur signale clairement cette dépendance.
- **Encapsulation du namespace** : ça évite de polluer l'espace de noms global avec une classe `Moteur` qui pourrait entrer en conflit avec un `Moteur` d'un autre contexte (par exemple un moteur de recherche).
- **Lisibilité** : en lisant `class Voiture`, on voit immédiatement que le concept de `Moteur` lui appartient.

### Ce qui se passe à l'exécution

1. `Voiture("Lamborghini", 640, "essence")` crée d'abord un objet `Moteur(640, "essence")`, stocké dans `self.moteur`.
2. `lambo.demarrer()` affiche la marque puis appelle `self.moteur.demarrer()`, qui affiche les infos du moteur.
3. `lambo.moteur.puissance` accède directement à l'attribut `puissance` de l'objet `Moteur` imbriqué dans `lambo`.

### À retenir

Une classe imbriquée reste une classe normale (avec `__init__`, des méthodes, etc.). Ce qui change, c'est **où elle est déclarée** et **la relation de dépendance** qu'elle exprime avec la classe qui la contient.
