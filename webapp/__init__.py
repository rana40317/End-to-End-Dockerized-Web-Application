from flask import Flask
from webapp.database import get_connection

def create_app():
    app = Flask(__name__)
    from webapp.routes import api
    app.register_blueprint(api)

    return app

def initialize_database():
    conn= get_connection()
    cursor=conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL,status VARCHAR(255) NOT NULL
    );

""")

    conn.commit()
    cursor.close()
    conn.close()


