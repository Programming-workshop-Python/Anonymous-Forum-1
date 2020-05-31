from psycopg2 import sql
from first import db


class TreadRepository:
    @staticmethod
    def create_tread(name, board_id):
        with db.cursor() as cursor:
            db.autocommit = True
            values = [
                (name, board_id)
            ]
            insert = sql.SQL(
                'INSERT INTO tread (name) VALUES {}').format(
                sql.SQL(',').join(map(sql.Literal, values))
            )
            cursor.execute(insert)
        print("create")