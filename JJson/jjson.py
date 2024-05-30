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

    # signup

    def is_uniqe_user(self, username):
        data = self.load_json_file()
        for each_user in data:
            if username == each_user:
                return False
        return True

    def is_uniqe_category(self, category, username):
        data = self.load_json_file()
        if username not in data.keys():
            data[username] = []
            self.save_to_json(data)
            return True
        for category_item in data[username]:
            if category_item == category:
                return False
        return True

    def is_uniqe_email(self, email):
        data = self.load_json_file()
        for each_user in data:
            if data[each_user]["email"] == email:
                return False
        return True

    def is_uniqe_phone(self, phone):
        data = self.load_json_file()
        for each_user in data:
            if data[each_user]["phone"] == phone:
                return False
        return True

    # login

    def does_user_exist(self, emuser, password):
        check_result = ""
        data = self.load_json_file()
        for each_user in list(data.keys()):
            if each_user == emuser or data[each_user]["email"] == emuser:
                if password == data[each_user]["password"]:
                    return "Valid"
                else:
                    return "invalid password"
            else:
                check_result = "not found"
        return check_result

    def does_user_exist_for_forgotpage(self, emuser):
        check_result = ""
        data = self.load_json_file()
        for each_user in list(data.keys()):
            if each_user == emuser or data[each_user]["email"] == emuser:
                return "Valid"
            else:
                check_result = "not found"
        return check_result

    def finding_email(self, email):
        data = self.load_json_file()
        for each_user in data.keys():
            if data[each_user]["email"] == email:
                return True
        return False

    def get_user_by_email(self, email):
        data = self.load_json_file()
        for each_user in data.keys():
            if email == each_user:
                return each_user
            elif email == data[each_user]["email"]:
                return each_user

    def return_list_of_category(self, user):
        data = self.load_json_file()
        if user in data:
            if len(data[user]) != 0:
                return list(data[user])
            else:
                return []
        else:
            return []

    def return_records(self, user):
        data = self.load_json_file()
        if user not in data:
            data[user] = {
                "amount": [],
                "date": [],
                "resource": [],
                "type": [],
                "description": [],
            }
        return data[user]
