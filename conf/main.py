import os
import sqlite3
import csv





class Database:
    def __init__(self):
        self._conn = sqlite3.connect("Americadbb.db")  #CONNECTION à la base de donnée
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def last_id(self):
        return self.cursor.lastrowid()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def queryOne(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchone()



files = {
    "DataAnalyst.csv": "Analyst",
    #"2020_Data_Professional_Salary_Survey_Responses.xlsx": "Salary",

}



with Database() as db:
    for file, table_name in files.items():
        with open(f'Data/01_raw/{file}', 'r') as data_file:
            reader = csv.reader(data_file)
            for i, row in enumerate(reader):
                if i == 0:
                    fields = row