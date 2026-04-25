# 🍔 BurgerDash

Un jeu de fast-food 2D simple développé avec **Python** et **Pygame**.

---

## 📋 Description

Dans **BurgerDash**, tu incarnes un employé dans un restaurant de fast-food.  
Un client apparaît et passe une commande (burger, frites ou boisson).  
Tu dois cliquer sur le bon aliment avant que le temps ne soit écoulé !

---

## 🎮 Comment jouer

1. Lance le jeu avec `python main.py`
2. Clique sur **START GAME** pour commencer
3. Regarde la commande affichée au-dessus du client
4. Clique sur l'image correspondante parmi les 3 boutons en bas de l'écran
5. Chaque bonne réponse rapporte **+1 point**
6. Un mauvais choix ou un délai dépassé entraîne le **Game Over**

---

## ⚙️ Règles

| Situation | Résultat |
|-----------|----------|
| Bon aliment cliqué | +1 point, nouvelle commande |
| Mauvais aliment cliqué | Game Over |
| Temps écoulé (5 secondes) | Game Over |

---

## 🗂️ Structure du projet

```
BurgerDash/
├── main.py         ← Boucle de jeu, interface, événements
├── objects.py      ← Classes Button, Customer, Order
└── assets/
    ├── background.png
    ├── burger.png
    ├── fries.png
    ├── drink.png
    └── customer.png
```

---

## 🚀 Lancement

### Prérequis

- Python 3.10 ou supérieur
- Pygame

### Installation de Pygame

```bash
pip install pygame
```

### Démarrer le jeu

```bash
python main.py
```

---

## 🛠️ Technologies utilisées

- **Python 3.10+**
- **Pygame** — moteur graphique 2D

---

## 👤 Auteur

Projet réalisé à titre éducatif.
