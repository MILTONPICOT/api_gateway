import json
import re
import requests

HEADERS = {"Content-Type": "application/json; charset=utf-8"}


def load_file_config() -> dict:
    """

    :return:
    """
    with open("config.json", 'r') as file_:
        data = json.load(file_)  # lee el contenido de un archivo json y lo guarda como un diccionario phyton
    return data


def clean_url(url: str) -> str:
    """
    :param url:
    :return:
    """

    segments = url.split('/')
    for segment in segments:
        if re.search('\\d', segment):
            url = url.replace(segment, "?")
    return url


def validate_grant(endpoint: str, method: str, id_rol: int) -> bool:
    """

    :param endpoint:
    :param method:
    :param id_rol:
    :return:
    """
    has_grant = False
    data_config = load_file_config()
    url = data_config.get('url-backend-security') + "/rol/validate/" + str(id_rol)
    body = {
        "url": endpoint,
        "method": method
    }
    print(url)
    print(body)
    response = requests.get(url, headers=HEADERS, json=body)
    print(response.json())
    try:
        if response.status_code == 200:
            has_grant = True
    except Exception as e:
        print(e)
    return has_grant
