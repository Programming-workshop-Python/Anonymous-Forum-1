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
                'INSERT INTO tread (name, board_id) VALUES {}').format(
                sql.SQL(',').join(map(sql.Literal, values))
            )
            cursor.execute(insert)
        print("create")

    @staticmethod
    def get_tread_by_board(board_id):
        ret = {}
        with db.cursor() as cursor:
            db.autocommit = True
            cursor.execute('SELECT * FROM tread WHERE tread.board_id = %s;', board_id)
            for row in cursor:
                ret[row[0]] = {
                    'name': row[1],
                    'board_id': row[2]
                }
        return ret
