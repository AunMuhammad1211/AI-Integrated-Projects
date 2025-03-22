import folium
from folium.plugins import MarkerCluster

def generate_map_alert(coordinates, output_path="output/herd_map.html"):
    herd_map = folium.Map(location=[37.7749, -122.4194], zoom_start=10)
    marker_cluster = MarkerCluster().add_to(herd_map)
    for lat, lon in coordinates:
        folium.Marker(
            location=[lat, lon],
            popup="Herd Detected!",
            icon=folium.Icon(color="red", icon="exclamation-triangle")
        ).add_to(marker_cluster)
    
    herd_map.save(output_path)
    print(f"Map with alerts saved to {output_path}")
    
    if coordinates:
        print("ALERT: Herd detected! Check the map for locations.")
    else:
        print("No herd detected.")