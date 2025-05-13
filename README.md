# Weather in Jalisco Locations Using Open-Meteo

This is a Python script that retrieves current weather information for several municipalities in the state of Jalisco, Mexico, using the free [Open-Meteo](https://open-meteo.com/) API.

## Description

The program displays an interactive menu in the terminal, allowing the user to select a location. Using its geographic coordinates, it queries the Open-Meteo API to retrieve current weather data and displays:

- Weather description (e.g., clear, light rain, fog, etc.)
- Current temperature in degrees Celsius
- Wind speed in km/h

It also maps numeric weather codes returned by the API to human-readable descriptions.

## Included Locations

The script currently supports the following locations:

- Arandas  
- Tepatitlán  
- Valle de Guadalupe  
- Yahualica  

## Requirements

- Python 3.6 or higher  
- `requests` library

You can install the required dependency with:

```bash
pip install requests
```
## Usage

1. **Download or clone the repository**.

2. **Run the script from the terminal**:

    ```bash
    python clima_jalisco.py
    ```

3. **Choose a location from the menu** to get the current weather.

## Code Structure

- `LUGARES`: Dictionary with location names and geographic coordinates.
- `CODIGOS_CLIMA`: Dictionary mapping weather codes to readable descriptions.
- `obtener_clima()`: Function that queries the API and returns a summary of the weather.
- `main()`: Main function that contains the interactive menu logic.
