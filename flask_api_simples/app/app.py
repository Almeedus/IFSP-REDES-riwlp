from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuração da conexão com o banco de dados
db_config = {
    'user': 'root',
    'password': 'admin123',
    'host': 'mysql_db',
    'database': 'email_user'
}

def insert_email(email):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO emails (email) VALUES (%s)", (email,))
        conn.commit()
    except Error as err:
        print(f"Error: {err}")
        return False
    finally:
        cursor.close()
        conn.close()
    return True

@app.route('/enviar_email', methods=['POST'])
def enviar_email():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email não fornecido'}), 400

    if insert_email(email):
        return jsonify({'message': 'Email enviado com sucesso!'}), 201
    else:
        return jsonify({'error': 'Falha ao enviar email'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
