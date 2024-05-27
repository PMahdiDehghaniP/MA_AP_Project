import json

class CreateJson:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_json_file(self):
        try:
            with open(self.file_name, "r") as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        return data

    def save_to_json(self, data):
        with open(self.file_name, "w") as json_file:
            json.dump(data, json_file)

    def add_dict_to_json(self, new_dict):
        existing_data = self.load_json_file()
        existing_data.update(new_dict)
        self.save_to_json(existing_data)
