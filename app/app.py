from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
#CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'p'

mysql = MySQL(app)

# Ruta para obtener los datos desde el frontend
@app.route('/api/obtener_datos', methods=['GET'])
def obtener_datos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT name, price, link, img FROM test")
    resultados = cur.fetchall()
    cur.close()

    datos = []
    for fila in resultados:
        producto = {
            "image": fila[3],
            "title": fila[0],
            "price": fila[1],
            "link": fila[2]
        }
        datos.append(producto)


   

    response = jsonify(datos)
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:8080")
    return response



if __name__ == '__main__':
    app.run(debug=True)
