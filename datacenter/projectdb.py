import sqlite3 as sql


class PDataBase():
    def __init__(self):
        self.Connector = sql.connect("project_database.db")
        self.command = self.Connector.cursor()
        self.create_userinfo_table()
        self.create_income_user_table()
        self.create_cost_user_table()
        self.create_category_table()

    def create_userinfo_table(self):
        self.command.execute('''CREATE TABLE IF NOT EXISTS UserInfo(
            username TEXT NOT NULL UNIQUE,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phonenumber TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            city TEXT NOT NULL,
            birthday TEXT NOT NULL
        )''')
        self.Connector.commit()

    def create_income_user_table(self):
        self.command.execute('''CREATE TABLE IF NOT EXISTS UserIncome(
            username TEXT NOT NULL UNIQUE,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            resource TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT NOT NULL UNIQUE,
            CHECK (length(description) <= 100)
        )''')
        self.Connector.commit()

    def create_cost_user_table(self):
        self.command.execute('''CREATE TABLE IF NOT EXISTS UserCost(
            username TEXT NOT NULL UNIQUE,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            resource TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT NOT NULL UNIQUE,
            CHECK (length(description) <= 100)
        )''')
        self.Connector.commit()

    def create_category_table(self):
        self.command.execute('''CREATE TABLE IF NOT EXISTS UserCategories(
            username TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL
        )''')
        self.Connector.commit()

    def add_new_user(self, fname, lname, phonenumber, username, password, city, email, date):
        self.command.execute('''
        INSERT INTO UserInfo (username,firstname,lastname,email,phonenumber,password,city,birthday) VALUES (?,?,?,?,?,?,?,?)''',
                             (username, fname, lname, email, phonenumber, password, city, date))
        self.Connector.commit()

    def add_new_IC(self, IC, username, amount, date, resource, type, description):
        self.command.execute(f'''
        INSERT INTO {IC} (username,amount,date,resource,type,description) VALUES (?,?,?,?,?,?)''',
                             (username, amount, date, resource, type, description))
        self.Connector.commit()

    def add_category(self, username, category_name):
        self.command.execute('''
        INSERT INTO UserCategories (username,category) VALUES (?,?)''',
                             (username, category_name))
        self.Connector.commit()

    def isunique_username(self, username):
        self.command.execute(
            'SELECT COUNT(*) FROM UserInfo WHERE username=?', (username,))
        count = self.command.fetchone()[0]
        return count == 0

    def isunique_phonenumber(self, phonenumber):
        self.command.execute(
            'SELECT COUNT(*) FROM UserInfo WHERE phonenumber=?', (phonenumber,))
        count = self.command.fetchone()[0]
        return count == 0

    def isunique_email(self, email):
        self.command.execute(
            'SELECT COUNT(*) FROM UserInfo WHERE email=?', (email,))
        count = self.command.fetchone()[0]
        return count == 0

    def isunique_category(self, username, category_name):
        self.command.execute(
            'SELECT COUNT(*) FROM UserCategories WHERE username=? AND category=?', (username, category_name))
        count = self.command.fetchone()[0]
        return count == 0
