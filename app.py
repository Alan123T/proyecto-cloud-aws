from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        # Validar que todas las variables de entorno estén definidas
        db_host = os.getenv("DB_HOST")
        db_user = os.getenv("DB_USER")
        db_pass = os.getenv("DB_PASS")
        db_name = os.getenv("DB_NAME")
        
        if not all([db_host, db_user, db_pass, db_name]):
            return "<h1>Error de Configuración</h1><p>Faltan variables de entorno necesarias: DB_HOST, DB_USER, DB_PASS, DB_NAME</p>"
        
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name
        )
        conn.close()
        return "<h1>Conexion Exitosa</h1><p>La app Flask se conecto a RDS correctamente.</p>"
    except Exception as e:
        return f"<h1>Error de Conexion</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
