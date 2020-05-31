from psycopg2 import sql
from first import db


class BoardRepository:
    @staticmethod
    def create_board(name):
        with db.cursor() as cursor:
            db.autocommit = True
            values = [
                (name)
            ]
            insert = sql.SQL(
                'INSERT INTO board (name) VALUES ({})').format(
                sql.SQL(',').join(map(sql.Literal, values))
            )
            cursor.execute(insert)
        print("create")


    @staticmethod
    def get_all_boards():
        ret = {}
        with db.cursor() as cursor:
            db.autocommit = True
            cursor.execute('SELECT * FROM board;')
            for row in cursor:
                ret[row[0]] = {
                    'name': row[1]
                }
        return ret

    @staticmethod
    def get_board(id):
        ret = {}
        with db.cursor() as cursor:
            db.autocommit = True
            cursor.execute('SELECT * FROM board WHERE board.id = %s;', id)
            for row in cursor:
                ret[row[0]] = {
                    'name': row[1]
                }
        return ret


    @staticmethod
    def edit_board(id, name):
        with db.cursor() as cursor:
            db.autocommit = True
            cursor.execute('UPDATE board SET name = %s WHERE id = %s',
                           (name, id))
        print("edit board with id %s", id)