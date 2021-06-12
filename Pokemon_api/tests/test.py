import pytest
import requests


def test_rest_api_code():
    headers = {
        "content-type": "application/json; charset=utf-8",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    url = 'http://127.0.0.1:8000/get/13'
    response = requests.get(url=url, headers=headers)
    assert response.status_code == 200


def test_rest_api_response():
    headers = {
        "content-type": "application/json; charset=utf-8",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    url = 'http://127.0.0.1:8000/get/13'
    moves = '["bug-bite", "electroweb", "poison-sting", "string-shot"]'
    response = requests.get(url=url, headers=headers)
    assert response.text == moves
