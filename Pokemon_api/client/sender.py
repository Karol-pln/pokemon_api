import requests


def send_requests_to_nameko():
    pokemon_id = 0
    while True:
        try:
            pokemon_id = int(input("Enter your Pokemon ID: "))
            if pokemon_id < 0:
                print("Pokemon ID cannot take negative values, enter a positive value")
                continue
            break
        except:
            print("Invalid pokemon ID. Please try again")
            continue

    headers = {
        "content-type": "application/json; charset=utf-8",
        "Accept": "*/*",
    }
    url = 'http://localhost:8000/get/' + str(pokemon_id)
    try:
        response = requests.get(url=url, headers=headers)
        return print("The attacks of the selected pokemon: " + response.text)
    except requests.exceptions.ConnectionError:
        return "Cant connect to nameko api"


if __name__ == "__main__":
    send_requests_to_nameko()
