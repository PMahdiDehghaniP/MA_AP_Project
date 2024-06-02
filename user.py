import re


class User:
    Users=[]
    def __init__(
        self,
        name,
        lastname,
        username,
        phone,
        password,
        email,
        city,
        birthday,
        question="",
    ):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.phone = phone
        self.password = password
        self.email = email
        self.city = city
        self.birthday = birthday
        self.question = question

