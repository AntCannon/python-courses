import pytest
from main_06 import get_weather


# call mocker
def test_get_weather(mocker):
    # Mock requests.get
    mock_get = mocker.patch("main_06.requests.get")

    # Set return values
    # from the response return the status code value
    mock_get.return_value.status_code = 200

    # from the response return the json value
    # from json return value
    # json is a function so has access to the return_value
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    # Call function using hte mock config
    result = get_weather("Dubai")

    # Assertions
    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")
