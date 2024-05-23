# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:42:38 2024

@author: Chancy
"""
import ee
import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

ee.Authenticate()
# Initialize Earth Engine
ee.Initialize()

# Function to calculate water area for an image
def water_area(image):
    date = ee.Date(image.get('system:time_start')).format('YYYY-MM-dd')
    # Compute water area within the region of interest
    water_area = image.reduceRegion(ee.Reducer.sum(), geojson['features'][0]['geometry'], scale=30, maxPixels=1e9)
    return ee.Feature(None, {
        'date': date,
        'water': water_area.get('water')
    })

if __name__ == "__main__":

    # Prompt user to enter start date, end date, and GeoJSON file path
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    geojson_file = input("Enter path to the GeoJSON file: ")

    # Load GeoJSON file
    with open(geojson_file, 'r') as f:
        geojson = json.load(f)

    # Load the JRC Global Surface Water dataset for the specified time range
    water_dataset = ee.ImageCollection("JRC/GSW1_3/MonthlyHistory").filterDate(start_date, end_date)

    # Map over the image collection to calculate water area
    water_areas = water_dataset.map(water_area).getInfo()['features']

    # Convert the result to a DataFrame
    water_df = pd.DataFrame([{
        'date': datetime.strptime(feature['properties']['date'], '%Y-%m-%d'),
        'water_area': feature['properties']['water']
    } for feature in water_areas])

    # Plot the time series
    plt.figure(figsize=(10, 6))
    plt.plot(water_df['date'], water_df['water_area'], marker='o')
    plt.title('Water Extent Time Series')
    plt.xlabel('Time')
    plt.ylabel('Water Area (m2)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('water_extent_time_series.png')
    plt.show()

