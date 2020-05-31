from flask import Flask
import psycopg2


def create_app():
    app = Flask(__name__)
    return app


def connect_db():
    return psycopg2.connect(
        dbname='anonymous_forum',
        user='postgres',
        password='123',
        host='localhost',
        port=5432
    )


app = create_app()
db = connect_db()
