from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

politicalparty_blueprints = Blueprint("politicalparty_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-votos') + "/politicalParty"


@politicalparty_blueprints.route("/politicalpartys", methods=['GET'])
def get_all_politicalpartys() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@politicalparty_blueprints.route("/politicalparty/<string:id_>", methods=['GET'])
def get_politicalparty_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@politicalparty_blueprints.route("/politicalparty/insert", methods=['POST'])
def insert_politicalparty() -> dict:
    politicalparty = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=politicalparty)
    return response.json()


@politicalparty_blueprints.route("/politicalparty/update/<string:id_>", methods=['PUT'])
def update_politicalparty(id_: str) -> dict:
    politicalparty = request.get_json()
    url = url_base + f'/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=politicalparty)
    return response.json()


@politicalparty_blueprints.route("/politicalparty/delete/<string:id_>", methods=['DELETE'])
def delete_politicalparty(id_: str) -> dict:
    url = url_base + f'/delete/{id_}'
    response = requests.delete(url, headers=HEADERS)
    return response.json()

