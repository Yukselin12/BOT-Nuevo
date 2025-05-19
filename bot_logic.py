import requests
import random    


def get():
    url = "https://uselessfacts.jsph.pl/random.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["text"]
    else:
        return "No se pudo obtener la information, intente de nuevo"