# Tout comprendre sur `round()` en Python 🐍

Ce guide explique le fonctionnement de la fonction `round()`, ses pièges (comme le *banker's rounding*) et son application concrète pour l'exercice `python01/ex2/ft_plant_growth.py`.

---

## 📌 Syntaxe de base

```python
round(nombre, ndigits=None)
```

* **`nombre`** : Le nombre flottant (`float`) ou entier (`int`) à arrondir.
* **`ndigits`** *(optionnel)* : Le nombre de décimales souhaitées après la virgule.

---

## 🛠️ Utilisation de `round()`

### 1. Sans le deuxième argument (`ndigits`)
Sans préciser le nombre de décimales, `round()` arrondit à l'**entier le plus proche** et retourne un type **`int`** (pas un `float`).

```python
round(25.6)  # 26
round(25.4)  # 25
round(25.5)  # 26
```

### 2. Avec le deuxième argument
Ici, `ndigits` précise le nombre de décimales à conserver. Le résultat reste un **`float`**.

```python
round(25.876, 1)  # 25.9
round(25.876, 2)  # 25.88
round(25.0, 1)    # 25.0
```

---

## ⚠️ Les pièges classiques à connaître

### Le "Banker's Rounding" (Arrondi bancaire)
C'est le point le plus surprenant de Python. Python n'utilise pas l'arrondi mathématique classique (où `.5` monte toujours). Il utilise l'**arrondi au chiffre pair le plus proche** (*round-half-to-even*).

```python
round(0.5)  # 0 (et pas 1 !)
round(1.5)  # 2
round(2.5)  # 2 (et pas 3 !)
round(3.5)  # 4
```
💡 **Pourquoi ce choix ?** Cette convention évite les biais statistiques. Si on arrondissait toujours le `.5` vers le haut, la moyenne d'un grand ensemble de données serait artificiellement gonflée.

### L'imprécision des nombres flottants (`float`)
Parfois, le résultat semble faux, mais cela est dû à la façon dont les ordinateurs stockent les nombres en mémoire (binaire).

```python
round(2.675, 2)  # Donne 2.67 au lieu de 2.68 !
```
En mémoire, `2.675` est stocké sous la forme d'une valeur infiniment plus petite (ex: `2.67499999...`). L'arrondi se fait donc vers le bas. C'est une limite matérielle commune à presque tous les langages de programmation.

---

## 🪴 Application concrète : `ft_plant_growth.py`

### Le problème
Dans l'exercice, si la croissance journalière d'une plante est de `0.8 cm` et que l'on fait `self.height += 0.8` en boucle, l'imprécision des floats va vite créer des nombres illisibles comme `26.600000000000001`.

L'énoncé demande pourtant un affichage propre :
* *Rose: 25.8cm, 31 days old*
* *Rose: 26.6cm, 32 days old*

### La solution
Il faut utiliser `round(valeur, 1)` après chaque calcul pour nettoyer le résultat avant l'affichage.

```python
# Exemple de code propre
height = 25.0
height += 0.8
height = round(height, 1)

print(height)  # Affiche proprement : 25.8
```
