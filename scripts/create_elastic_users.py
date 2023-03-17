import random
import string

import requests

from config import ELASTIC_PASSWORD, ELASTIC_USERNAME, ELASTIC_ENDPOINT

AUTH = (ELASTIC_USERNAME, ELASTIC_PASSWORD)

ROLE_MAPPINGS = [
    {
        "username": "learning_catalogue",
        "role": {
            "name": "learning_catalogue_indices",
            "indices": ["courses", "lpg-feedback", "lpg-learning-providers", "media"]
        }
    }
]


def make_request(_method, endpoint, json):
    full_url = f"{ELASTIC_ENDPOINT}/_security/{endpoint}"
    req = requests.Request(method=_method, url=full_url, auth=AUTH, json=json)
    with requests.Session() as s:
        prepared_request = req.prepare()
        try:
            res = s.send(prepared_request)
            print(res.json())
            res.raise_for_status()
            return res
        except Exception as e:
            print(f"{_method} request to {full_url} failed: {e}")


def create_role(role_obj):
    url = f"role/{role_obj['name']}"
    req_json = {
        "cluster": ["all"],
        "indices": [
            {
                "names": role_obj["indices"],
                "privileges": ["all"]
            }
        ]
    }
    make_request("POST", url, req_json)


def create_user(username, role_name):
    password = generate_password()
    url = f"user/{username}"
    req_json = {
        "password": password,
        "roles": ["editor", role_name],
        "full_name": username,
    }
    make_request("POST", url, req_json)


def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for i in range(10))


def run():
    print(f"Creating {len(ROLE_MAPPINGS)} roles")
    for role_mapping in ROLE_MAPPINGS:
        print(f"Creating role {role_mapping['username']}")
        create_role(role_mapping['role'])
        create_user(role_mapping['username'], role_mapping['role']['name'])