import boto3
from flask import Flask, jsonify

# Configurar conexión con DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Ajusta tu región
tabla = dynamodb.Table('DiasSemana')  # Asegúrate de usar el nombre correcto de tu tabla

# Inicializar Flask
app = Flask(__name__)

@app.route('/dias', methods=['GET'])
def obtener_dias():
    respuesta = tabla.scan()  # Consulta todos los registros de la tabla
    dias = [{"id": item["id"], "dia": item["dia"]} for item in respuesta["Items"]]
    return jsonify({"dias": dias})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Permite acceder desde otras máquinas
