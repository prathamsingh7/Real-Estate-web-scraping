from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)
db_params = {
    "host": "localhost",
    "database": "PropReturns",
    "user": "postgres",
    "password": "******",
    "port": 5432,
}

@app.route('/get_data_by_document_no', methods=['GET'])

def get_data_by_document_no():
    document_no = request.args.get('document_number')
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Real_Estate" WHERE "document_number" = %s', (document_no,))
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/get_data_by_year_of_registration', methods=['GET'])

def get_data_by_year_of_registration():
    year_of_registration = request.args.get('reg_year')
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Real_Estate" WHERE "reg_year" = %s', (year_of_registration,))
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)