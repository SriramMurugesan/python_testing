import requests

def get_weather(city):
    """Get weather for a specific city.
    
    Args:
        city (str): The city to get weather for
        
    Returns:
        dict: Weather data
        
    Raises:
        ValueError: If the request fails
    """
    url = f"https://api.weather.com/v1/{city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Failed to get weather")