from flask import Blueprint,jsonify
from webapp.database import get_connection

api = Blueprint("api",__name__)

@api.route("/health",methods=["GET"])
def health():
    return jsonify({"status":"healthy" }),200

@api.route("/api/tasks", methods=["GET"])

def get_tasks():
    conn= get_connection()
    cursor= conn.cursor()
    cursor.execute("SELECT id, title, status FROM tasks ORDER BY id;")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()

    task=[]
    for row in rows:
        task.append({"id":row[0],"title":row[1],"status":row[2]})
    return jsonify([{ "id":1,"title": "Docker", "status": "Going on"},{ "id":2, "title": "CI/CD", "status": "Going on"}]),200



