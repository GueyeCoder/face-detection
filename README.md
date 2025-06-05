# Détection de Visages avec OpenCV

Ce projet implémente plusieurs techniques de détection de visages et d'yeux en utilisant OpenCV et les classificateurs Haar Cascade en Python.

## 🎯 Fonctionnalités

- **Détection de visages** : Détection automatique des visages dans les images
- **Détection d'yeux** : Détection et localisation des yeux sur les visages
- **Échange de visages** : Application amusante qui échange les visages entre deux personnes dans une image
- **Extraction de visages** : Extraction et affichage séparé de chaque visage détecté

## 📁 Structure du projet

```
face-detect/
├── app.py                                 # Application d'échange de visages
├── face-detection.py                      # Script de détection de visages
├── eye-detection.py                       # Script de détection d'yeux
├── haarcascade_frontalface_default.xml    # Classificateur Haar pour visages
├── haarcascade_eye.xml                    # Classificateur Haar pour yeux
└── README.md                              # Documentation du projet
```

## 🚀 Installation

### Prérequis

- Python 3.6+
- OpenCV

### Installation des dépendances

```bash
# Installer OpenCV
pip install opencv-python

# Ou avec conda
conda install -c conda-forge opencv
```

## 📖 Utilisation

### 1. Détection de visages (`face-detection.py`)

Ce script détecte les visages dans une image et les affiche avec des rectangles verts.

```bash
python face-detection.py
```

**Fonctionnalités :**
- Détecte tous les visages dans l'image `obama.jpg`
- Dessine des rectangles verts autour des visages détectés
- Extrait et affiche chaque visage dans une fenêtre séparée

### 2. Détection d'yeux (`eye-detection.py`)

Ce script détecte à la fois les visages et les yeux dans une image.

```bash
python eye-detection.py
```

**Fonctionnalités :**
- Détecte les visages (rectangles verts)
- Détecte les yeux (rectangles bleus)
- Affiche l'image avec toutes les détections

### 3. Échange de visages (`app.py`)

Application amusante qui échange les visages entre deux personnes dans une image.

```bash
python app.py
```

**Fonctionnalités :**
- Détecte exactement 2 visages dans l'image `brad-angelina.jpg`
- Échange automatiquement les visages entre les deux personnes
- Redimensionne les visages pour un ajustement optimal

## 🖼️ Images requises

Pour faire fonctionner les scripts, vous devez ajouter les images suivantes dans le répertoire du projet :

- `obama.jpg` - Pour les scripts de détection de visages et d'yeux
- `brad-angelina.jpg` - Pour l'application d'échange de visages (doit contenir exactement 2 visages)

## ⚙️ Paramètres techniques

### Classificateurs Haar Cascade

- **haarcascade_frontalface_default.xml** : Détection de visages frontaux
- **haarcascade_eye.xml** : Détection d'yeux

### Paramètres de détection

- `scaleFactor` : 1.1 (facteur d'échelle pour la détection multi-échelle)
- `minNeighbors` : 3-8 (nombre minimum de voisins requis pour une détection)

## 🛠️ Personnalisation

### Modifier les paramètres de détection

```python
# Ajuster la sensibilité de détection
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,     # Réduire pour plus de précision (ex: 1.05)
    minNeighbors=5,      # Augmenter pour moins de faux positifs
    minSize=(30, 30),    # Taille minimale des visages
    maxSize=(300, 300)   # Taille maximale des visages
)
```

### Changer les couleurs des rectangles

```python
# Couleurs BGR (Blue, Green, Red)
cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Vert
cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Bleu
cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)  # Rouge
```

## 🔧 Dépannage

### Erreur "Deux visages requises"
Cette erreur se produit dans `app.py` si l'image ne contient pas exactement 2 visages. Vérifiez que :
- L'image `brad-angelina.jpg` existe
- L'image contient exactement 2 visages clairement visibles
- L'éclairage de l'image est suffisant

### Aucun visage détecté
Si aucun visage n'est détecté :
- Vérifiez que l'image existe et est lisible
- Ajustez les paramètres `scaleFactor` et `minNeighbors`
- Assurez-vous que les visages sont frontaux et bien éclairés

## 📚 Concepts utilisés

- **Classificateurs Haar Cascade** : Technique d'apprentissage automatique pour la détection d'objets
- **Détection multi-échelle** : Détection à différentes tailles d'objets
- **Traitement d'images** : Conversion en niveaux de gris, redimensionnement
- **OpenCV** : Bibliothèque de vision par ordinateur

## 🎓 Améliorations possibles

- [ ] Ajouter la détection en temps réel via webcam
- [ ] Implémenter d'autres classificateurs (profil, sourire, etc.)
- [ ] Ajouter la reconnaissance faciale
- [ ] Créer une interface graphique
- [ ] Optimiser les performances pour le traitement vidéo
- [ ] Ajouter la détection d'émotions
