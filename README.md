# World Clock and Weather Data Application

This project includes a Streamlit application that displays world clocks across multiple time zones and fetches real-time weather data using external APIs. It also demonstrates how to store and retrieve weather data from a SQLite database.

## Features

- **World Clock**: Displays the current time in selected time zones.
- **Weather Data**: Fetches and displays real-time temperature data for specified locations using latitude and longitude.
- **Data Storage**: Stores weather data in a SQLite database for historical tracking and analysis.

## Getting Started

### Prerequisites

- Python 3.6+
- Streamlit
- Requests
- BeautifulSoup4 (optional, if scraping)
- Geopy (optional, for geolocation features)
- SQLite3

### Installation

1. Clone the repository to your local machine.

  ```
git clone https://github.com/yahanna/510lab4final.git
  ```
2. Install the required Python packages.
  ```
pip install streamlit requests beautifulsoup4 geopy sqlite3
  ```
### Running the Application

To run the Streamlit application, navigate to the directory containing `app.py` and execute the following command:

  ```
streamlit run app.py
  ```

## Usage

### World Clock

- The application allows users to select up to 4 time zones from a dropdown menu to display the current time.

### Weather Data Fetching

- Weather data can be fetched by specifying the latitude and longitude of the desired location.
- The application uses the National Weather Service API (or any other specified API) to fetch real-time temperature data.

### Data Storage

- The SQLite database `world.db` contains tables for storing location details and weather data.
- The `data.py` script demonstrates how to insert fetched weather data into the database.

## Database Schema

The SQLite database includes the following tables:

- `locations`: Stores location details including city name, country, and timezone.
- `weather_data`: Stores weather data including temperature, humidity, and weather description, linked to locations.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
