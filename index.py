import requests
import json
import dash
import dash_leaflet as dl
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Clé API
api_key = "e0a1bf2c844edb9084efc764c089dd748676cc14"

# Fonction pour récupérer les données de l'API
def get_data(api_key):
    url = f"https://api.jcdecaux.com/vls/v1/stations?apiKey={api_key}"
    response = requests.get(url)
    return response.json()


# Afficher les données dans la console
data = get_data(api_key)
print(json.dumps(data, indent=4))


# Fonction pour calculer les statistiques de vélos
def calculate_stats(data):
    bike_stats = {"mechanical": 0, "ebike": 0}
    city_bike_count = {}
    
    for station in data:
        city = station["contract_name"]
        available_bikes = station["available_bikes"]

        bike_stats["mechanical"] += station["available_bike_stands"]
        bike_stats["ebike"] += station["available_ebike_stands"] if "available_ebike_stands" in station else 0

        if city not in city_bike_count:
            city_bike_count[city] = available_bikes
        else:
            city_bike_count[city] += available_bikes

    bike_stats["total"] = bike_stats["mechanical"] + bike_stats["ebike"]
    bike_stats["mechanical_percentage"] = (bike_stats["mechanical"] / bike_stats["total"]) * 100
    bike_stats["ebike_percentage"] = (bike_stats["ebike"] / bike_stats["total"]) * 100

    return bike_stats, city_bike_count



# Fonction pour créer les marqueurs de la carte
def create_markers(data):
    markers = []
    for station in data:
        tooltip = f"{station['name']}<br>Vélos disponibles: {station['available_bikes']}"
        markers.append(
            dl.Marker(position=[station["position"]["lat"], station["position"]["lng"]], children=tooltip)
        )
    return markers


# Création de l'application Dash
app = dash.Dash(__name__)

# Mise en page de l'application
app.layout = html.Div([
    html.H1("Vélos en libre-service"),
    dcc.Interval(id='interval-component', interval=60 * 1000, n_intervals=0),  # Mise à jour toutes les minutes
    dl.Map(id="map", style={'width': '100%', 'height': '500px'}, center=[45.7597, 4.8422], zoom=12),
])

# Fonction de callback pour mettre à jour la carte
@app.callback(
    Output("map", "children"),
    [Input("interval-component", "n_intervals")],
)
def update_map(n):
    data = get_data(api_key)
    # # Récupérer les données
    data = get_data(api_key)

    # Calculer les statistiques
    bike_stats, city_bike_count = calculate_stats(data)
    print(f"Pourcentage de vélos mécaniques: {bike_stats['mechanical_percentage']:.2f}%")
    print(f"Pourcentage de vélos électriques: {bike_stats['ebike_percentage']:.2f}%")

    # Classement des villes avec le plus de vélos
    sorted_city_bike_count = dict(sorted(city_bike_count.items(), key=lambda item: item[1], reverse=True))
    print("\nClassement des villes avec le plus de vélos disponibles:")
    for city, count in sorted_city_bike_count.items():
        print(f"{city}: {count}")
    markers = create_markers(data)
    return markers

# Lancement de l'application
if __name__ == "__main__":  # Corrigé ici
    app.run_server(debug=True)
