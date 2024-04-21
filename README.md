# PARTIE THEORIQUE DU TEST 
1) Une API (Application Programming Interface) est un ensemble de règles et de spécifications que les applications peuvent suivre pour communiquer entre elles.
Exemple, Google Maps Platform est l'une des API de cartographie les plus utilisées et les plus complètes. Elle offre de nombreuses fonctionnalités, y compris l'affichage de cartes personnalisables, le géocodage, les itinéraires, et les informations sur le trafic.

2) Un webhook est un moyen pour une application d'envoyer des informations en temps réel à d'autres applications dès qu'un événement donné se produit. Fonctionnant comme une sorte de "push notification" pour les serveurs, il envoie des données à une URL spécifiée en réponse à des événements. 
Exemple d'utilisation :Dans le contexte du développement d'applications de gestion des réservations de billets de voyage, un webhook peut être extrêmement utile pour plusieurs raisons, notamment pour: les notifications en temps réels, mise à jour automatique des reservations

3) Les bases de données relationnelles, comme MySQL ou PostgreSQL, stockent les données dans des tables structurées et les relations entre ces tables sont définies par des clés étrangères. Elles sont idéales pour des données fortement structurées et des requêtes complexes alors que  Les bases de données non relationnelles (ou NoSQL), comme MongoDB ou Cassandra ont des tables non-structurées et  utilisent une approche plus flexible qui peut inclure des documents, des graphes, ou des colonnes larges. Elles sont adaptées pour gérer de grandes quantités de données.

4) Oui, j'ai utilisé Python dans plusieurs projets. Python est un langage de programmation interprété, dynamique et polyvalent.
 Mes expériences avec Python incluent le développement web avec Django, l'automatisation de scripts, et le traitement de données avec des bibliothèques telles que Pandas et NumPy.

5) Oui j'ai déjà utilisé le CMS wordpress pour la création des sites web.


# Détails explicatif de la partie pratique du test

1) Importation des bibliothèques nécessaires : requests pour envoyer des requêtes HTTP à l'API, json pour manipuler les données JSON, dash pour créer l'application web, dash_leaflet pour ajouter une carte interactive à l'application, dcc et html pour créer des composants de l'interface utilisateur, et Input, Output pour définir les interactions entre les composants.

2) Définition de la clé API pour accéder à l'API de JCDecaux, qui fournit des données sur les vélos en libre-service.

3) Définition d'une fonction get_data(api_key) pour récupérer les données de l'API en envoyant une requête GET à l'URL de l'API avec la clé API.

4) Définition d'une fonction calculate_stats(data) pour calculer les statistiques sur les vélos disponibles dans chaque ville et le pourcentage de vélos mécaniques et électriques. La fonction renvoie un dictionnaire bike_stats avec les statistiques et un dictionnaire city_bike_count avec le nombre de vélos disponibles dans chaque ville.

5) Définition d'une fonction create_markers(data) pour créer des marqueurs sur la carte pour chaque station de vélos disponible dans les données.

6) Création de l'application Dash avec app = dash.Dash(_name_).

7) Définition de la mise en page de l'application avec app.layout. La mise en page comprend un titre, un composant dcc.Interval pour mettre à jour les données toutes les minutes, et un composant dl.Map pour afficher la carte interactive.

8) Définition d'une fonction de callback update_map(n) pour mettre à jour la carte avec les nouvelles données toutes les minutes. La fonction récupère les données à partir de l'API, calcule les statistiques, crée des marqueurs pour chaque station de vélos disponible, et renvoie les marqueurs à afficher sur la carte.

9) Lancement de l'application avec app.run_server(debug=True) si le script est exécuté en tant que programme principal
