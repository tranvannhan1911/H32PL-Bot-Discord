import sqlite3
import csv
import unicodedata
class DB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        self.conn.execute(
            'CREATE TABLE IF NOT EXISTS codeforce_handle ('
            'id       TEXT,'
            'handle   TEXT'
            ')'
        )
        

    def check_exists(self, table, where, value):
        query = (
            'SELECT 1 '
            'FROM {0} '.format(table) +
            'WHERE {0} = ?'.format(where)
        )
        res = self.conn.execute(query, (value, )).fetchone()
        return res is not None


    # for local debug
    def get_data(self, table, limit = 10):
        query = (
            'SELECT * '
            'FROM {0} '.format(table)
        )
        if limit is not None:
            query +=  'LIMIT {0}'.format(limit)
        x = self.conn.execute(query).fetchall()
        return x

    # handle codeforce
    def add_handle(self, id, handle):
        if self.check_exists("codeforce_handle", "id", id) == False:
            query = (
                'INSERT INTO codeforce_handle (id, handle) '
                'VALUES (?, ?)'
            )
            self.conn.execute(query, (id, handle))
            self.conn.commit()
            return True

        return False

    

    def update_handle(self, id, handle):
        if self.check_exists("codeforce_handle", "id", id) == True:
            print("update")
            query = (
                'UPDATE codeforce_handle SET handle = ? where id = ?'
            )
            self.conn.execute(query, (handle, id))
            self.conn.commit()
            return True
        else:
            return self.add_handle(id, handle)

    def get_handle(self, id):
        query = (
            'SELECT handle from codeforce_handle where id = ?'
        )
        res = self.conn.execute(query, (id, )).fetchone()
        return res[0]

database = DB('database/database.db')
