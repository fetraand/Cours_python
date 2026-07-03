# Les Méthodes Statiques (`@staticmethod`)

## Code

```python
class Voiture:
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    @staticmethod
    def show():
        print("Voiture de lux:")

    @staticmethod
    def kmh_to_mph(vitesse_kmh):
        return vitesse_kmh * 0.621371

    @staticmethod
    def est_prix_raisonnable(prix):
        return prix < 100000


lambo = Voiture("Lamborghini", 250, 200000)

lambo.show()
print(Voiture.kmh_to_mph(lambo.vitesse))
print(Voiture.est_prix_raisonnable(lambo.prix))

```

### Sortie attendue

```
Voiture de lux:
155.34275
False
```

## Explication du Code et des Concepts

Cet exemple introduit les **méthodes statiques** (`@staticmethod`), le troisième type de méthode en POO après les méthodes d'instance et les méthodes de classe.

### Le décorateur `@staticmethod`

Une méthode d'instance reçoit `self`, une méthode de classe reçoit `cls`. Une méthode statique, elle, **ne reçoit ni l'un ni l'autre** :

```python
@staticmethod
def kmh_to_mph(vitesse_kmh):
    return vitesse_kmh * 0.621371
```

Elle se comporte comme une fonction normale, sauf qu'elle est rangée à l'intérieur de la classe parce qu'elle est **liée logiquement** à celle-ci.

### Pourquoi ne pas juste utiliser `self` ou `cls` ?

Parce que la méthode n'a besoin ni de l'objet (`self`), ni de la classe (`cls`) pour fonctionner. Elle ne lit et ne modifie aucun attribut de l'instance ou de la classe. C'est un pur calcul ou une pure vérification à partir des paramètres qu'on lui donne.

Exemple : convertir une vitesse de km/h en mph ne dépend d'aucune voiture en particulier, c'est juste une formule mathématique.

### Différence avec `classmethod`

| Type | Premier paramètre | Accès à l'objet | Accès à la classe | Usage typique |
|---|---|---|---|---|
| Méthode d'instance | `self` | Oui | Indirect | Manipuler les données d'un objet précis |
| Méthode de classe | `cls` | Non | Oui | Constructeur alternatif, créer des instances |
| Méthode statique | Aucun | Non | Non | Fonction utilitaire liée au thème de la classe |

### Comment on l'appelle

On peut appeler une méthode statique directement sur la classe :

```python
Voiture.kmh_to_mph(250)
```

ou sur une instance (ça fonctionne aussi, mais l'instance n'est pas utilisée à l'intérieur) :

```python
lambo.kmh_to_mph(250)
```

### Ce qui se passe à l'exécution

1. `Voiture.kmh_to_mph(lambo.vitesse)` prend `250` et calcule `250 * 0.621371`, ce qui donne `155.34275`.
2. `Voiture.est_prix_raisonnable(lambo.prix)` vérifie si `200000 < 100000`, ce qui est `False`.

### En résumé

On utilise `@staticmethod` quand une fonction a un lien logique avec la classe (elle sert à quelque chose en rapport avec des voitures), mais qu'elle **n'a besoin d'aucune donnée propre à un objet ou à la classe** pour s'exécuter.
