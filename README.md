
# Taxi Data Visualization

🚖 **Taxi Data Visualization** is an interactive Streamlit application designed for exploring and analyzing taxi pickup and dropoff data, along with temporal and spatial trends of taxi rides in New York City. The project leverages various visualization techniques including scatter plots, datashader maps, and choropleth maps to provide insightful views into taxi data.

---

## 📝 Features

1. **Interactive Maps**:
    - Pickup and dropoff locations for both Green and Yellow taxis visualized using datashader.
    - Scatter plots with adjustable layers for comparing taxi pickups and dropoffs.

2. **Choropleth Maps**:
    - Frequency of taxi rides by zones for both Green and Yellow taxis.
    
3. **Temporal Analysis**:
    - Average number of rides per hour for each day of the week displayed as a line chart.

4. **Image Layer Adjustment**:
    - Blend and adjust opacity of image layers for detailed spatial analysis.

---

## 📂 Project Structure

```
├── app.py                  # Main application script
├── data/                   # Data folder containing CSV and GeoJSON files
│   ├── GreenDataResize.csv
│   ├── YellowDataResize.csv
│   ├── vtc_zone_freq.geojson
│   ├── YellowVTC_Zone_Freq.csv
│   ├── GreenVTC_Zone_Freq.csv
│   ├── grouped_by_minute.csv
├── images/                 # Processed images folder
│   ├── final_image_dropoff_yellow.png
│   ├── final_image_pickup_yellow.png
│   ├── final_image_pickup_green.png
├── .gitignore              # Ignored files for Git
├── README.md               # Project README file
├── requirements.txt        # Python dependencies
```

---

## 🚀 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/taxi-data-visualization.git
    cd taxi-data-visualization
    ```

2. Install required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

---

## 📊 Data Sources

- **Taxi Data**: Processed CSV files for Green and Yellow taxis, including pickup and dropoff details.
- **Spatial Data**: GeoJSON file for taxi zones and their frequencies.

---

## 🌟 Usage

- **Left Panel**: Explore interactive maps and visualizations for taxi data trends.
- **Sidebar**: Adjust image layers to analyze spatial overlaps.

---

## 🛠 Requirements

- Python 3.8+
- Streamlit
- Plotly
- Pandas
- Datashader
- PIL (Pillow)
- colorcet

---

## 📜 License

This project is licensed under the MIT License.

---

## 🏗 Future Enhancements

- Add real-time data integration.
- Extend to include other cities.
- Improve temporal analysis with advanced time-series modeling.

---

## 📬 Contact

For any inquiries or suggestions, please contact [your-email@example.com].
