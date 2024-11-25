###############################################
# Importer les bibliothèques
###############################################
import streamlit as st
import pandas as pd
import datashader as ds
import datashader.transfer_functions as tf
import plotly.graph_objects as go
from colorcet import fire
from PIL import Image
import plotly.express as px
import json

###############################################
# Step 2 : Configurer la mise en page Streamlit
###############################################
st.set_page_config(layout="wide", page_title="Taxi Data Visualization", page_icon="🚖")
left_column, right_column = st.columns([7, 3])

###############################################
# Step 3 : Colonne gauche --> Carte principale
###############################################

with left_column:
    st.header("Taxi Data Visualization")

    # Load datasets
    gtaxi = pd.read_csv('data/GreenDataResize.csv', low_memory=False)
    ytaxi = pd.read_csv('data/YellowDataResize.csv', low_memory=False)
    

    # ======== Combined Visualization: Pickup and Dropoff Locations ========
    st.subheader("Comparison of Green and Yellow Taxi")

    # First Row: Pickup Locations
    st.markdown("#### Pickup Locations")
    pickup_col1, pickup_col2 = st.columns(2)  # Create two columns for pickups

    # Green Taxi Pickup Visualization
    with pickup_col1:
        st.write("**Green Taxi Pickup Locations**")
        # Prepare data
        df = gtaxi.rename(columns={'Pickup_latitude': 'Lat', 'Pickup_longitude': 'Lon'})
        df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
        df['Lon'] = pd.to_numeric(df['Lon'], errors='coerce')
        dff = df.query('Lat < 40.92').query('Lat > 40.60').query('Lon > -74.15').query('Lon < -73.75')

        # Datashader grid
        cvs = ds.Canvas(plot_width=1500, plot_height=1500)
        agg = cvs.points(dff, x='Lon', y='Lat')

        # Get image and coordinates
        coords_lat, coords_lon = agg.coords['Lat'].values, agg.coords['Lon'].values
        coordinates = [
            [coords_lon[0], coords_lat[0]],
            [coords_lon[-1], coords_lat[0]],
            [coords_lon[-1], coords_lat[-1]],
            [coords_lon[0], coords_lat[-1]]
        ]
        img = tf.shade(agg, cmap=fire)[::-1].to_pil()

        # Plotly map
        fig = px.scatter_mapbox(dff[:1], lat='Lat', lon='Lon', zoom=10)
        fig.update_layout(
            mapbox_style="carto-darkmatter",
            mapbox_center={"lat": 40.78, "lon": -73.95},
            mapbox_layers=[
                {
                    "sourcetype": "image",
                    "source": img,
                    "coordinates": coordinates,
                }
            ],
            width=400,
            height=550
        )
        st.plotly_chart(fig, use_container_width=True)

    # Yellow Taxi Pickup Visualization
    with pickup_col2:
        st.write("**Yellow Taxi Pickup Locations**")
        # Prepare data
        df = ytaxi.rename(columns={'pickup_latitude': 'Lat', 'pickup_longitude': 'Lon'})
        df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
        df['Lon'] = pd.to_numeric(df['Lon'], errors='coerce')
        dff = df.query('Lat < 40.92').query('Lat > 40.60').query('Lon > -74.15').query('Lon < -73.75')

        # Datashader grid
        cvs = ds.Canvas(plot_width=1500, plot_height=1500)
        agg = cvs.points(dff, x='Lon', y='Lat')

        # Get image and coordinates
        coords_lat, coords_lon = agg.coords['Lat'].values, agg.coords['Lon'].values
        coordinates = [
            [coords_lon[0], coords_lat[0]],
            [coords_lon[-1], coords_lat[0]],
            [coords_lon[-1], coords_lat[-1]],
            [coords_lon[0], coords_lat[-1]]
        ]
        img = tf.shade(agg, cmap=fire)[::-1].to_pil()

        # Plotly map
        fig = px.scatter_mapbox(dff[:1], lat='Lat', lon='Lon', zoom=10)
        fig.update_layout(
            mapbox_style="carto-darkmatter",
            mapbox_center={"lat": 40.78, "lon": -73.95},
            mapbox_layers=[
                {
                    "sourcetype": "image",
                    "source": img,
                    "coordinates": coordinates,
                }
            ],
            width=400,
            height=550
        )
        st.plotly_chart(fig, use_container_width=True)

    # Second Row: Dropoff Locations
    st.markdown("#### Dropoff Locations")
    dropoff_col1, dropoff_col2 = st.columns(2)  # Create two columns for dropoffs

    # Green Taxi Dropoff Visualization
    with dropoff_col1:
        st.write("**Green Taxi Dropoff Locations**")
        # Prepare data
        df = gtaxi.rename(columns={'Dropoff_latitude': 'Lat', 'Dropoff_longitude': 'Lon'})
        df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
        df['Lon'] = pd.to_numeric(df['Lon'], errors='coerce')
        dff = df.query('Lat < 40.92').query('Lat > 40.60').query('Lon > -74.15').query('Lon < -73.75')

        # Datashader grid
        cvs = ds.Canvas(plot_width=1500, plot_height=1500)
        agg = cvs.points(dff, x='Lon', y='Lat')

        # Get image and coordinates
        coords_lat, coords_lon = agg.coords['Lat'].values, agg.coords['Lon'].values
        coordinates = [
            [coords_lon[0], coords_lat[0]],
            [coords_lon[-1], coords_lat[0]],
            [coords_lon[-1], coords_lat[-1]],
            [coords_lon[0], coords_lat[-1]]
        ]
        img = tf.shade(agg, cmap=fire)[::-1].to_pil()

        # Plotly map
        fig = px.scatter_mapbox(dff[:1], lat='Lat', lon='Lon', zoom=10)
        fig.update_layout(
            mapbox_style="carto-darkmatter",
            mapbox_center={"lat": 40.78, "lon": -73.95},
            mapbox_layers=[
                {
                    "sourcetype": "image",
                    "source": img,
                    "coordinates": coordinates,
                }
            ],
            width=400,
            height=550
        )
        st.plotly_chart(fig, use_container_width=True)

    # Yellow Taxi Dropoff Visualization
    with dropoff_col2:
        st.write("**Yellow Taxi Dropoff Locations**")
        # Prepare data
        df = ytaxi.rename(columns={'dropoff_latitude': 'Lat', 'dropoff_longitude': 'Lon'})
        df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
        df['Lon'] = pd.to_numeric(df['Lon'], errors='coerce')
        dff = df.query('Lat < 40.92').query('Lat > 40.60').query('Lon > -74.15').query('Lon < -73.75')

        # Datashader grid
        cvs = ds.Canvas(plot_width=1500, plot_height=1500)
        agg = cvs.points(dff, x='Lon', y='Lat')

        # Get image and coordinates
        coords_lat, coords_lon = agg.coords['Lat'].values, agg.coords['Lon'].values
        coordinates = [
            [coords_lon[0], coords_lat[0]],
            [coords_lon[-1], coords_lat[0]],
            [coords_lon[-1], coords_lat[-1]],
            [coords_lon[0], coords_lat[-1]]
        ]
        img = tf.shade(agg, cmap=fire)[::-1].to_pil()

        # Plotly map
        fig = px.scatter_mapbox(dff[:1], lat='Lat', lon='Lon', zoom=10)
        fig.update_layout(
            mapbox_style="carto-darkmatter",
            mapbox_center={"lat": 40.78, "lon": -73.95},
            mapbox_layers=[
                {
                    "sourcetype": "image",
                    "source": img,
                    "coordinates": coordinates,
                }
            ],
            width=400,
            height=550
        )
        st.plotly_chart(fig, use_container_width=True)

    

    # ======== DIV 2: Scatter Mapbox of Pickups and Dropoffs ========
    st.subheader("Taxi Pickups and Dropoffs Overview")

    # Sampling data for visualization
    ytaxi_Viz_1 = ytaxi.sample(frac=0.01, random_state=42)
    gtaxi_Viz_1 = gtaxi.sample(frac=0.01, random_state=42)

    # Create the plot
    fig = go.Figure()

    fig.add_trace(go.Scattermapbox(
        lat=ytaxi_Viz_1['pickup_latitude'],
        lon=ytaxi_Viz_1['pickup_longitude'],
        mode='markers',
        marker=dict(size=5, color='yellow', opacity=0.4),
        name='Yellow Taxi Pickups'
    ))

    fig.add_trace(go.Scattermapbox(
        lat=ytaxi_Viz_1['dropoff_latitude'],
        lon=ytaxi_Viz_1['dropoff_longitude'],
        mode='markers',
        marker=dict(size=5, color='orange', opacity=0.4),
        name='Yellow Taxi Dropoffs'
    ))

    fig.add_trace(go.Scattermapbox(
        lat=gtaxi_Viz_1['Pickup_latitude'],
        lon=gtaxi_Viz_1['Pickup_longitude'],
        mode='markers',
        marker=dict(size=5, color='lightgreen', opacity=0.4),
        name='Green Taxi Pickups'
    ))

    fig.add_trace(go.Scattermapbox(
        lat=gtaxi_Viz_1['Dropoff_latitude'],
        lon=gtaxi_Viz_1['Dropoff_longitude'],
        mode='markers',
        marker=dict(size=5, color='green', opacity=0.4),
        name='Green Taxi Dropoffs'
    ))

    fig.update_layout(
        mapbox=dict(
            style="carto-darkmatter",
            zoom=10,
            center=dict(lat=40.730610, lon=-73.935242)
        ),
        width=1300,
        height=600,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        legend=dict(title="Taxi Type")
    )

    st.plotly_chart(fig, use_container_width=True)

    # ======== DIV 3: Choropleth Visualization ========
    st.subheader("VTC Taxi Zone Frequency by Type")

    with open('data/vtc_zone_freq.geojson') as f:
        geojson = json.load(f)

    # Diviser les données par type de taxi
    yellow_taxi = pd.read_csv('data/YellowVTC_Zone_Freq.csv')
    green_taxi = pd.read_csv('data/GreenVTC_Zone_Freq.csv')

    # Create the plot
    fig = go.Figure()

    fig.add_trace(go.Choroplethmapbox(
        geojson=geojson,
        featureidkey="properties.zone",
        locations=yellow_taxi['zone'],
        z=yellow_taxi['frequency'],
        colorscale="YlOrRd",
        colorbar_title="Frequency (Yellow Taxis)",
        marker_opacity=0.7,
        name="Yellow Taxis"
    ))

    fig.add_trace(go.Choroplethmapbox(
        geojson=geojson,
        featureidkey="properties.zone",
        locations=green_taxi['zone'],
        z=green_taxi['frequency'],
        colorscale="Greens",
        colorbar_title="Frequency (Green Taxis)",
        marker_opacity=0.7,
        name="Green Taxis"
    ))

    fig.update_layout(
        mapbox=dict(
            style="carto-positron",
            center={"lat": 40.730610, "lon": -73.935242},
            zoom=9
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )


    st.plotly_chart(fig, use_container_width=True)



    # ======== DIV 4: Analyse temporelle ========
    st.subheader("Average Temporal Evolution of the Number of Taxi Rides per Hour for Each Day of the Week")

    # Charger les données
    grouped_by_minute = pd.read_csv('data/grouped_by_minute.csv')

    fig = px.line(
    grouped_by_minute,
    x="minute",  # Utiliser la colonne sans date
    y="frequency",
    color="Journalier",  # Couleur par jour de la semaine
    title="Number of Rides per Minute and per Day of the Week",
    labels={
        "Minute": "Heure de la journée",
        "Frequency": "Fréquence",
        "Jour": "Jour de la semaine"
    },
    height=800,
    width=1300
    )


    fig.update_layout(
        xaxis=dict(
            tickmode='linear',  # Mode de ticks linéaire
            dtick=120,  # Un tick toutes les 15 minutes (900 secondes)
            title_text="Heure de la journée",  # Titre clair pour l'axe X
            tickangle=45  # Incliner les labels pour éviter le chevauchement
        ),
        yaxis=dict(
            title_text="Nombre de Courses"  # Titre clair pour l'axe Y
        ),
        legend_title="Jour de la semaine"
    )


    st.plotly_chart(fig, use_container_width=True)

    


###############################################
# Step 4 : Colonne Slider --> Images Analysis
###############################################
with st.sidebar:
    st.title("Analysis of the 3 Base Images")
    

    # Charger les images (vérifiez les chemins)
    dropoff_yellow_img = Image.open("images/final_image_dropoff_yellow.png").convert("RGBA")
    pickup_yellow_img = Image.open("images/final_image_pickup_yellow.png").convert("RGBA")
    pickup_green_img = Image.open("images/final_image_pickup_green.png").convert("RGBA")

    # Sliders pour ajuster les opacités
    st.subheader("Adjust Image Layers")
    dropoff_yellow_opacity = st.slider("Dropoff Yellow", 0, 100, 100) / 100
    pickup_yellow_opacity = st.slider("Pickup Yellow", 0, 100, 0) / 100
    pickup_green_opacity = st.slider("Pickup Green", 0, 100, 0) / 100

    # Fonction pour superposer les images avec des opacités
    def blend_images(base_image, overlay_image, opacity):
        """Superpose une image sur une image de base avec une opacité ajustée."""
        overlay = overlay_image.copy()
        overlay.putalpha(int(opacity * 255))
        return Image.alpha_composite(base_image, overlay)

    # Image de base transparente
    base_image = Image.new("RGBA", dropoff_yellow_img.size, (255, 255, 255, 0))

    # Ajouter les images en fonction des opacités
    base_image = blend_images(base_image, dropoff_yellow_img, dropoff_yellow_opacity)
    base_image = blend_images(base_image, pickup_yellow_img, pickup_yellow_opacity)
    base_image = blend_images(base_image, pickup_green_img, pickup_green_opacity)

    # Afficher l'image finale combinée
    st.image(base_image, caption="Superposed Images", use_container_width=True)
