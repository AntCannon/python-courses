import pytest
from main_08 import UserService, APIClient


def test_get_username_with_mock(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)  # Create a mock API client

    # Mock get_user_data to return a fake user
    mock_api_client.get_user_data.return_value = {"id": 1, "name": "Alice"}

    service = UserService(mock_api_client)  # Inject mock API client

    result = service.get_username(1)  # Call method that depends on the mock

    # Assertions
    assert result == "ALICE"  # Check if processing was done correctly
    mock_api_client.get_user_data.assert_called_once_with(
        1
    )  # Ensure correct API was called


def test_get_user_email_with_mock(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)

    mock_api_client.get_user_data.return_value = {
        "user_id": 2,
        "name": "Tony",
        "email": "tony@example.com",
    }

    service = UserService(mock_api_client)

    result = service.get_user_email(2)

    assert result == "tony@example.com"
    mock_api_client.get_user_data.assert_called_once_with(2)
