""""
pokemon sozdanie
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json', "trainer_token": "db7106629449659ae33d026a72bc5d61"}

body = {
    "name": "Кобра",
   "photo": "https://dolnikov.ru/pokemons/albums/005.png"
}

body1 ={
   "pokemon_id": "28464",
   "name": "Albina",
  "photo": "https://dolnikov.ru/pokemons/albums/006.png"
}

body2={
    "pokemon_id": "28464"
}

response = requests.post(url=f'{URL}//pokemons',json=body,headers=HEADER,timeout=5)
print(f'Статус код: {response.status_code}.Сообщение: {response.json()["message"]}')

response = requests.put(url=f'{URL}//pokemons',json=body1,headers=HEADER,timeout=5)
print(f'Статус код: {response.status_code}.Сообщение: {response.json()["message"]}')

response = requests.post(url=f'{URL}//trainers/add_pokeball',json=body2,headers=HEADER,timeout=5)
print(f'Статус код: {response.status_code}.Сообщение: {response.json()["message"]}')

