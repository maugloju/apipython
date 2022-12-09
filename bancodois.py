from flask import Flask, request
import mysql.connector
import json

#con = mysql.connector.connect(host='bdunifeob.c9snstumptjo.sa-east-1.rds.amazonaws.com', database='webservice', user='admin', password='rdsteteia')
con = mysql.connector.connect(host='localhost', database='webservice', user='root', password='')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado', db_info)
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

@app.route("/validator", methods=["POST"])

def validator():
    body = request.json

    valida = " SELECT * FROM UN_VW_DADOS_ACESSO WHERE  matricula = %s AND senha = %s "
    val = (body["usuario"], body["senha"])

    cursor = con.cursor(dictionary=True)
    cursor.execute(valida, val)
    userdata = cursor.fetchone()
    return json.dumps(userdata)

    if con.is_connected():
        cursor2.close()
        con.close()
        print('Conexão encerrada')

app.run(debug=True)