import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json,"trainer_token": "db7106629449659ae33d026a72bc5d61"'}

body = {
    "trainer_token": "db7106629449659ae33d026a72bc5d61",
    "email": "evgeniya.sytina@mail.ru",
    "password": "Varvara13032014"
}

def test_get_trainers():
    """
    get trainers
    """
    response = requests.get(url = f'{URL}/trainers', json=body, headers=HEADER, timeout=10)
    assert response.status_code == 200

def test_get_trainers_id():
    """
    get trainers_id
    """
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id':'3880'},json=body, headers=HEADER, timeout=10)
    assert response.json()['trainer_name'] == 'токен'
