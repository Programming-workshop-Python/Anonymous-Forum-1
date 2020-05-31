from psycopg2 import sql
from first import db


class MessageRepository:
    @staticmethod
    def create_message(author, text, tread_id):
        with db.cursor() as cursor:
            db.autocommit = True
            values = [
                (author, text, tread_id)
            ]
            insert = sql.SQL(
                'INSERT INTO message (name) VALUES {}').format(
                sql.SQL(',').join(map(sql.Literal, values))
            )
            cursor.execute(insert)
        print("create")
