import pytest
from mock.main import get_weather

def test_get_weather_success(mocker):
    # Mock the requests.get method
    mock_get = mocker.patch("requests.get")
    
    # Set up the mock response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"weather": "Hot", "condition": "Sunny"}
    mock_get.return_value = mock_response
    
    # Call the function
    result = get_weather("London")
    
    # Assert the results
    assert result == {"weather": "Hot", "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/London")

def test_get_weather_failure(mocker):
    # Mock the requests.get method to return an error status code
    mock_get = mocker.patch("requests.get")
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    
    # Test that the function raises ValueError on failure
    with pytest.raises(ValueError, match="Failed to get weather"):
        get_weather("InvalidCity")