from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
        )
        return "<h1>Conexion Exitosa</h1><p>La app Flask se conecto a RDS correctamente.</p>"
    except Exception as e:
        return f"<h1>Error de Conexion</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)