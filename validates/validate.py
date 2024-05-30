import re


class Validate:
    def __init__(self) -> None:
        pass

    def validate_password(self, string):
        checkStr = ""
        lowercase_reg = re.compile(r"[a-z]")
        uppercase_reg = re.compile(r"[A-Z]")
        digit_reg = re.compile(r"[0-9]")
        symbol_reg = re.compile(r"[^(\w\d\s)]")
        if string == "":
            checkStr = False
        if not lowercase_reg.search(string):
            checkStr = False
        elif not uppercase_reg.search(string):
            checkStr = False
        elif not digit_reg.search(string):
            checkStr = False
        elif not symbol_reg.search(string):
            checkStr = False
        elif len(string) < 6:
            checkStr = False
        else:
            checkStr = True
        return checkStr

    def validate_name(self, name):
        checkuser = True
        if name.isalpha() and 3 < len(name) <= 15:
            checkuser = True
        elif len(name) == 0:
            checkuser = False
        else:
            checkuser = False
        return checkuser

    def validate_email(self, email):
        pattern = r"^[a-z]+\w*@gmail\.com"
        pattern2 = r"^[a-z]+\w*@yahoo\.com"
        checkEmail = (
            True if re.search(pattern, email) or re.search(
                pattern2, email) else False
        )
        if email == "":
            checkEmail = False
        return checkEmail

    def validite_birthday(self, date_string):
        pattern = r"^(19[2-9]\d|200[0-5])/(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])$"
        if re.match(pattern, date_string):
            return True
        else:
            return False

    def validate_phone_number(self, mobile_number):
        regex = r"^09\d{9}$"
        if re.match(regex, mobile_number):
            return True
        else:
            return False

    def validate_city(self, city):
        checkCity = False
        cityOpthoin = [
            "yazd",
            "tehran",
            "shiraz",
            """mash'had""",
            "abadan",
            "kermanshah",
            "bushehr",
            "ahvaz",
            "kordestan",
            "isfahan",
        ]

        for i in range(len(cityOpthoin)):
            if city == cityOpthoin[i]:
                checkCity = True
        return checkCity

    def validate_username(self, username):
        pattern = r"^(?=[a-zA-Z])[a-zA-Z0-9_]{5,}(?=.*\d)[a-zA-Z0-9_]*$"
        if re.match(pattern, username):
            return True
        else:
            return False

    def validate_date_income_cost(self, date):
        pattern = r"^(?:(?:19|20)\d\d)/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$"
        return bool(re.match(pattern, date))

    def validate_categoty(self, category):
        pattern = r'^(?=.*[a-zA-Z])[a-zA-Z0-9 ]{1,15}$'
        return bool(re.match(pattern, category))

    def valid_amount(self, amount):
        pattern = r'^[1-9]\d*$|^0$'
        return bool(re.match(pattern, amount))

    def valid_description(self, discription):
        if len(discription) <= 100:
            return True
        else:
            return False
