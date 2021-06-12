import json
import requests
from nameko.web.handlers import http


class PokemonMovesApi:
    name = "pokemon_moves_service"

    @http('GET', '/get/<int:pokemon_id>')
    def get_method(self, request, pokemon_id):
        return pokeapi_request(pokemon_id)


def pokeapi_request(pokemon_id):
    try:
        url = 'https://pokeapi.co/api/v2/pokemon/' + str(pokemon_id)
        moves_list = []
        headers = {
            "content-type": "application/json; charset=utf-8",
            "Accept": "*/*",
            "Connection": "keep-alive"
        }
        response = requests.get(url=url, headers=headers)
    except requests.exceptions.ConnectionError:
        return "Cant connect to pokeapi.co"

    if response.ok is False:
        return "Your pokemon cant be find"

    content = response.json()
    moves = content["moves"]

    for move in moves:
        moves_list.append(move["move"]["name"])

    return json.dumps(sorted(moves_list))
