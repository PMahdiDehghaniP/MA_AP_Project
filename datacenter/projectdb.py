import sqlite3 as sql


class PDataBase:
    def __init__(self):
        self.Connector = sql.connect("project_database.db")
        self.command = self.Connector.cursor()
        self.create_userinfo_table()
        self.create_income_user_table()
        self.create_cost_user_table()
        self.create_category_table()
        self.migrate_category_table()

    def create_userinfo_table(self):
        self.command.execute(
            """CREATE TABLE IF NOT EXISTS UserInfo(
            username TEXT NOT NULL UNIQUE,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phonenumber TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            city TEXT NOT NULL,
            birthday TEXT NOT NULL
        )"""
        )
        self.Connector.commit()

    def create_income_user_table(self):
        self.command.execute(
            """CREATE TABLE IF NOT EXISTS UserIncome(
            username TEXT NOT NULL UNIQUE,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            resource TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT NOT NULL UNIQUE,
            CHECK (length(description) <= 100)
        )"""
        )
        self.Connector.commit()

    def create_cost_user_table(self):
        self.command.execute(
            """CREATE TABLE IF NOT EXISTS UserCost(
            username TEXT NOT NULL UNIQUE,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            resource TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT NOT NULL UNIQUE,
            CHECK (length(description) <= 100)
        )"""
        )
        self.Connector.commit()

    def create_category_table(self):
        self.command.execute(
            """CREATE TABLE IF NOT EXISTS UserCategories(
            username TEXT NOT NULL,
            category TEXT NOT NULL,
            UNIQUE(username, category)
        )"""
        )
        self.Connector.commit()

    def migrate_category_table(self):
        self.command.execute("ALTER TABLE UserCategories RENAME TO UserCategories_old")
        self.create_category_table()
        self.command.execute(
            """
            INSERT INTO UserCategories (username, category)
            SELECT username, category FROM UserCategories_old
        """
        )
        self.command.execute("DROP TABLE UserCategories_old")
        self.Connector.commit()

    def add_new_user(
        self, fname, lname, phonenumber, username, password, city, email, date
    ):
        self.command.execute(
            """
        INSERT INTO UserInfo (username,firstname,lastname,email,phonenumber,password,city,birthday) VALUES (?,?,?,?,?,?,?,?)""",
            (username, fname, lname, email, phonenumber, password, city, date),
        )
        self.Connector.commit()

    def add_new_IC(self, IC, username, amount, date, resource, type, description):
        self.command.execute(
            f"""
        INSERT INTO {IC} (username,amount,date,resource,type,description) VALUES (?,?,?,?,?,?)""",
            (username, amount, date, resource, type, description),
        )
        self.Connector.commit()

    def category_exists(self, username, category_name):
        self.command.execute(
            "SELECT COUNT(*) FROM UserCategories WHERE username=? AND category=?",
            (username, category_name),
        )
        count = self.command.fetchone()[0]
        return count > 0

    def add_category(self, username, category_name):
        if not self.category_exists(username, category_name):
            self.command.execute(
                """
            INSERT INTO UserCategories (username, category) VALUES (?, ?)""",
                (username, category_name),
            )
            self.Connector.commit()

    def isunique_username(self, username):
        self.command.execute(
            "SELECT COUNT(*) FROM UserInfo WHERE username=?", (username,)
        )
        count = self.command.fetchone()[0]
        return count == 0

    def isunique_phonenumber(self, phonenumber):
        self.command.execute(
            "SELECT COUNT(*) FROM UserInfo WHERE phonenumber=?", (phonenumber,)
        )
        count = self.command.fetchone()[0]
        return count == 0

    def isunique_email(self, email):
        self.command.execute("SELECT COUNT(*) FROM UserInfo WHERE email=?", (email,))
        count = self.command.fetchone()[0]
        return count == 0

    def isunique_category(self, username, category_name):
        self.command.execute(
            "SELECT COUNT(*) FROM UserCategories WHERE username=? AND category=?",
            (username, category_name),
        )
        count = self.command.fetchone()[0]
        return count == 0

    def does_user_exist(self, username):
        self.command.execute(
            "SELECT COUNT(*) FROM UserInfo WHERE username=?", (username,)
        )
        count = self.command.fetchone()[0]
        return count > 0

    def return_list_of_category(self, username):
        self.command.execute(
            "SELECT category FROM UserCategories WHERE username=?", (username,)
        )
        categories = self.command.fetchall()
        return [category[0] for category in categories]

    def get_password(self, input_data):
        if "@" in input_data:
            self.command.execute(
                "SELECT password FROM UserInfo WHERE email=?", (input_data,)
            )
        else:
            self.command.execute(
                "SELECT password FROM UserInfo WHERE username=?", (input_data,)
            )
        password = self.command.fetchone()
        if password:
            return password[0]
        else:
            return None

    def return_username(self, input_data):
        self.command.execute(
            "SELECT username FROM UserInfo WHERE email=? OR username=?",
            (
                input_data,
                input_data,
            ),
        )
        username = self.command.fetchone()
        if username:
            return username[0]
        else:
            return False

    def return_email(self, input_data):
        self.command.execute(
            "SELECT email FROM UserInfo WHERE email=? OR username=?",
            (input_data, input_data),
        )
        email = self.command.fetchone()
        if email:
            return email[0]
        else:
            return False
