import json


def soil_test_payload():
    with open("/Users/amitkumar/Documents/BACKEND-PROJ/trimble-agri/test_data/soil_test.json", "r", ) as json_file:
        data = json.load(json_file)
        return json.dumps(data)


def update_soil_test_payload():
    with open("/Users/amitkumar/Documents/BACKEND-PROJ/trimble-agri/test_data/update_soil_test.json", "r", ) as \
            json_file:
        data = json.load(json_file)
        return json.dumps(data)
