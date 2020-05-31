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
                'INSERT INTO message (author, text, tread_id) VALUES {}').format(
                sql.SQL(',').join(map(sql.Literal, values))
            )
            cursor.execute(insert)
        print("create")


    @staticmethod
    def get_messages_by_tread(tread_id):
        ret = {}
        with db.cursor() as cursor:
            db.autocommit = True
            cursor.execute('SELECT * FROM message WHERE message.tread_id = %s;', tread_id)
            for row in cursor:
                ret[row[0]] = {
                    'name': row[1],
                    'text': row[2],
                    'tread_id': row[3],
                }
        return ret
