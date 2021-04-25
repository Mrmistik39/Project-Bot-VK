import sqlite3
from Utils.SqlItem import SqlItem


class Sqlite:
    TABLE = 'database'
    FILE = './database.db'

    connection = None

    INT = 'INTEGER'
    INT_AUTO = 'INT PRIMARY KEY'
    STR = 'TEXT'

    def open(self):
        self.connection = sqlite3.connect(self.FILE)
        self.create_table()

    def execute(self, text, array=None):
        self.open()
        sql = text.replace('$str', self.STR).replace('$int', self.INT).replace('$table', self.TABLE)
        if array is None:
            exe = self.connection.execute(sql)
        else:
            exe = self.connection.execute(sql, array)
        self.connection.commit()
        return exe

    def get_all(self) -> list:
        tuple_ = self.execute('SELECT * FROM $table')
        array = []
        for answer in tuple_:
            array.append(list(answer))
        return array

    def create_table(self):
        self.connection = sqlite3.connect(self.FILE)
        values = ', '.join([
            SqlItem('message', self.INT).__str__(),
            SqlItem('commands', self.INT).__str__(),
            SqlItem('user_id', self.INT).__str__()
        ])
        self.connection.execute(f'CREATE TABLE IF NOT EXISTS {self.TABLE}({values});')
        self.connection.commit()
