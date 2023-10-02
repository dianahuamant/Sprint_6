import configuration
import requests
import data
import json

# Aquí se crea un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Obteniendo auth_token del usuario
def get_auth_token():
    response = post_new_user(data.user_body)
    response_data = response.json()
    return response_data['authToken']

def send_post_request(kit_body):
    auth_token = get_auth_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT, headers=headers, json=kit_body)

    return response