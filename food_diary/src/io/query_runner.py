import sqlite3
from datetime import datetime

class QueryRunner(object):

    def __init__(self, config):
        self.config = config
        self.database_file_name = "%s\\%s.db" % (
            self.config.get("database_directory"),
            self.config.get("database_name")
        )

    def run_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        conn.execute(sql_str)
        conn.commit()

    def fetch_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        query = conn.execute(sql_str)
        results = query.fetchall()
        return results

    def create_all_tables(self):
        self.create_meals_table()

    def create_meals_table(self):
        sql_str = "CREATE TABLE meals(date DATE, text VARCHAR, type VARCHAR)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def insert_meal(self, meal_text, meal_type, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        sql_str = "INSERT INTO meals ('date', 'text', 'type') VALUES ('%s', '%s', '%s')" % (date, meal_text, meal_type)
        self.run_sql(sql_str)

    def get_meals(self, date=None):
        sql_str = "SELECT * FROM meals"
        if date is not None:
            sql_str += " WHERE date = '%s'" % date
        return self.fetch_sql(sql_str)
