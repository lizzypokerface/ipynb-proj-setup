import unittest.mock as mock

import pytest
from requests import HTTPError

import my_project.service.service as service


# https://docs.python.org/3/library/unittest.mock.html


@mock.patch("my_project.service.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    # mocking a function call
    mock_get_user_from_db.return_value = "Mocked Alice"
    assert service.get_user_from_db(1) == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    # mocking a property
    mock_response.status_code = 200
    # mocking a function call
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    # mocking a property
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(HTTPError):
        service.get_users()
