import sqlite3

class DB:
    def __init__(self):
        self.connection = sqlite3.connect('data.db')
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        try:
            query = 'CREATE TABLE posts (author, text, is_important)'
            self.cursor.execute(query)
            self.connection.commit()
        except:
            print('DB is here')

    def get_posts(self):
        query = 'SELECT * FROM posts'
        self.cursor.execute(query)
        response = self.cursor.fetchall()
        return response