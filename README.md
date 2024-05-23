# Surface Water Extent Time Series Analysis using Google Earth Engine

This Python script generates a surface water extent time series plot for a specified region of interest and time period using the Google Earth Engine (GEE) platform.

## Prerequisites

1. **Python**: Ensure Python is installed on your system. You can download and install Python from https://www.python.org/.

2. **Earth Engine Python API**: Install the Earth Engine Python API by following the instructions on the https://developers.google.com/earth-engine/guides/python_install.

3. **Required Python Packages**: Make sure you have the following Python packages installed:
   - `ee`
   - `pandas`
   - `matplotlib`
   
   You can install these packages via pip:

4. **Google Earth Engine Account**: You need a Google Earth Engine account to access the Earth Engine data. You can sign up for an account https://earthengine.google.com/.

## Usage

1. **Clone or download the script**: Clone this repository or download the script `surface_water_analysis.py`.

2. **Obtain a GeoJSON file**: Prepare a GeoJSON file representing the region of interest (ROI) for which you want to analyze the surface water extent. You can create or obtain a GeoJSON file using GIS software like QGIS or online GeoJSON editors.

3. **Run the script**: Open your terminal or command prompt, navigate to the directory containing the script, and run the script using Python:

4. **Follow the prompts**: The script will prompt you to enter the start date, end date, and the path to the GeoJSON file representing the ROI.

5. **View the output**: The script will generate a surface water extent time series plot and save it as `water_extent_time_series.png` in the same directory. Additionally, the plot will be displayed on your screen.

## Example

```bash
$ python surface_water_analysis.py
Enter start date (YYYY-MM-DD): 2020-01-01
Enter end date (YYYY-MM-DD): 2020-12-31
Enter path to the GeoJSON file: path/to/your/geojson/file.geojson
