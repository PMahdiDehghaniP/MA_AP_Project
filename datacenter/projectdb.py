import sqlite3 as sql
import pandas as pd
import os
import shutil


class PDataBase:
    def __init__(self):
        self.Connector = sql.connect("project_database.db")
        self.command = self.Connector.cursor()
        self.create_userinfo_table()
        self.create_income_user_table()
        self.create_cost_user_table()
        self.create_category_table()
        self.migrate_category_table()
        self.migrate_income_table()
        self.migrate_cost_table()

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
            username TEXT NOT NULL,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            resource TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT NOT NULL,
            CHECK (length(description) <= 100)
        )"""
        )
        self.Connector.commit()

    def create_cost_user_table(self):
        self.command.execute(
            """CREATE TABLE IF NOT EXISTS UserCost(
            username TEXT NOT NULL,
            amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            resource TEXT NOT NULL,
            type TEXT NOT NULL,
            description TEXT NOT NULL,
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

    def migrate_income_table(self):
        self.command.execute("ALTER TABLE UserIncome RENAME TO UserIncome_old")
        self.create_income_user_table()
        self.command.execute(
            """
            INSERT INTO UserIncome (username, amount, date, resource, type, description)
            SELECT username, amount, date, resource, type, description FROM UserIncome_old
        """
        )
        self.command.execute("DROP TABLE UserIncome_old")
        self.Connector.commit()

    def migrate_cost_table(self):
        self.command.execute("ALTER TABLE UserCost RENAME TO UserCost_old")
        self.create_cost_user_table()
        self.command.execute(
            """
            INSERT INTO UserCost (username, amount, date, resource, type, description)
            SELECT username, amount, date, resource, type, description FROM UserCost_old
        """
        )
        self.command.execute("DROP TABLE UserCost_old")
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

    def search_text(
        self,
        tables,
        username,
        text="",
        start_date=None,
        end_date=None,
        lower_price=None,
        higher_price=None,
        resource=None,
        item_type=None,
    ):
        final = ""
        for table in tables:
            self.command.execute(f"PRAGMA table_info({table})")
            columns = [column[1] for column in self.command.fetchall()]
            for column in columns:
                query = f"SELECT * FROM {table} WHERE username=? AND {column} LIKE ?"
                params = [username, "%" + text + "%"]
                if start_date and end_date and "date" in columns:
                    query += " AND date BETWEEN ? AND ?"
                    params.extend([start_date, end_date])
                if (
                    lower_price is not None
                    and higher_price is not None
                    and "amount" in columns
                ):
                    query += " AND amount BETWEEN ? AND ?"
                    params.extend([lower_price, higher_price])
                if resource and "resource" in columns:
                    query += " AND resource=?"
                    params.append(resource)
                if item_type and "type" in columns:
                    query += " AND type=?"
                    params.append(item_type)
                self.command.execute(query, params)
                results = self.command.fetchall()
                temp = ""
                if results:
                    for row in results:
                        temp += f"Results from {table}\n{row}\n"
                if temp not in final:
                    final += temp
        return final

    def delete_user_data(self, tables, username):
        for table in tables:
            self.command.execute(f"DELETE FROM {table} WHERE username=?", (username,))
        if any(self.command.rowcount == 0 for _ in tables):
            return False
        self.Connector.commit()
        return True

    def update_user_data(
        self,
        username,
        fname="",
        lname="",
        email="",
        phonenumber="",
        password="",
        city="",
        birthday="",
    ):
        fields = []
        values = []
        if email:
            fields.append("email=?")
            values.append(email)
        if fname:
            fields.append("firstname=?")
            values.append(fname)
        if lname:
            fields.append("lastname=?")
            values.append(lname)
        if phonenumber:
            fields.append("phonenumber=?")
            values.append(phonenumber)
        if password:
            fields.append("password=?")
            values.append(password)
        if city:
            fields.append("city=?")
            values.append(city)
        if birthday:
            fields.append("birthday=?")
            values.append(birthday)

        set_clause = ", ".join(fields)
        query = f"UPDATE UserInfo SET {set_clause} WHERE username=?"
        values.append(username)

        self.command.execute(query, values)
        self.Connector.commit()

    def export_csv_file(self, username):
        try:
            tables = pd.read_sql_query(
                "SELECT name FROM sqlite_master WHERE type='table';", self.Connector
            )
            base_folder = "Users_Csv_Data"
            user_folder = os.path.join(base_folder, f"{username}_Csv_Data")
            if not os.path.exists(user_folder):
                os.makedirs(user_folder)
            for table_name in tables["name"]:
                df_columns = pd.read_sql_query(
                    f"PRAGMA table_info({table_name});", self.Connector
                )
                if "username" in df_columns["name"].values:
                    query = f"SELECT * FROM {table_name} WHERE username = ?"
                    df = pd.read_sql_query(query, self.Connector, params=(username,))

                    if not df.empty:
                        csv_filename = os.path.join(
                            user_folder, f"{table_name}_{username}.csv"
                        )

                        if os.path.exists(csv_filename):
                            os.remove(csv_filename)
                        df.to_csv(csv_filename, index=False)
            return True
        except TypeError:
            return False

    def get_filtered_row_counts(
        self,
        tables,
        username,
        text="",
        start_date=None,
        end_date=None,
        lower_price=None,
        higher_price=None,
        resource=None,
        item_type=None,
    ):
        final_counts = {}
        for table in tables:
            self.command.execute(f"PRAGMA table_info({table})")
            columns = [column[1] for column in self.command.fetchall()]

            where_clauses = ["username=?"]
            params = [username]

            if text:
                text_conditions = [f"{column} = ?" for column in columns]
                text_params = [text for _ in columns]
                where_clauses.append(f"({' OR '.join(text_conditions)})")
                params.extend(text_params)

            if start_date and end_date and "date" in columns:
                where_clauses.append("date BETWEEN ? AND ?")
                params.extend([start_date, end_date])

            if (
                lower_price is not None
                and higher_price is not None
                and "amount" in columns
            ):
                where_clauses.append("amount BETWEEN ? AND ?")
                params.extend([lower_price, higher_price])

            if resource and "resource" in columns:
                where_clauses.append("resource=?")
                params.append(resource)

            if item_type and "type" in columns:
                where_clauses.append("type=?")
                params.append(item_type)

            where_clause = " AND ".join(where_clauses)

            query = f"SELECT COUNT(*) FROM {table} WHERE {where_clause}"
            self.command.execute(query, params)
            count = self.command.fetchone()[0]

            final_counts[table] = count
        total = 0
        for i in final_counts.keys():
            total += final_counts[i]
        final_counts["total"] = total
        return final_counts

    def get_row_count_for_user_in_table(self, table_name, username):
        query = f"SELECT COUNT(*) FROM {table_name} WHERE username=?"
        self.command.execute(query, (username,))
        result = self.command.fetchone()
        count = result[0] if result is not None else 0
        return count

    def delete_csv_file(self, username, table_name):
        base_folder = "Users_Csv_Data"
        user_folder = os.path.join(base_folder, f"{username}_Csv_Data")
        file_path = os.path.join(user_folder, f"{table_name}_{username}.csv")

        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def delete_all_csv_file(self, username):
        base_folder = "Users_Csv_Data"
        user_folder = os.path.join(base_folder, f"{username}_Csv_Data")
        if os.path.exists(user_folder):
            shutil.rmtree(user_folder)
            return True
        return False
