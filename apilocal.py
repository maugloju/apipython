from flask import Flask, request
import mysql.connector
import json

con = mysql.connector.connect(host='localhost', database='apiteste', user='root', password='')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado', db_info)

    cursor = con.cursor(dictionary=True)
    cursor.execute('select name, email from users limit 10')
    user_data = cursor.fetchall()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def respons_users():
    return {"users": list(user_data)}

@app.route("/users")
def list_users():
    return json.dumps(user_data)

if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão encerrada')

@app.route("/users", methods=["POST"])
def create_users():
    body = request.json
    con = mysql.connector.connect(host='localhost', database='apiteste', user='root', password='')

    if con.is_connected():
        db_info = con.get_server_info()
        print('Conectado', db_info)

    insert_cliente = " insert into users (name, email) values (%s,%s) "
    val = (body["name"], body["email"])

    cursor2 = con.cursor()
    cursor2.execute(insert_cliente, val)
    con.commit()
    print(cursor.rowcount)
    return respons_users()
if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão encerrada')



@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id):
    #user = user_id

    con = mysql.connector.connect(host='localhost', database='apiteste', user='root', password='')

    if con.is_connected():
        db_info = con.get_server_info()
        print('Conectado', db_info)

    delete_cliente = " DELETE FROM users WHERE  id = %s "
    val = (user_id,)

    cursor2 = con.cursor()
    cursor2.execute(delete_cliente, val)
    con.commit()
    return respons_users()


if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão encerrada')

 #   if user:
 #       del user_data[user_id]



@app.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id: int):
    body = request.json
    name = body["name"]
    email = body["email"]

    con = mysql.connector.connect(host='localhost', database='apiteste', user='root', password='')

    if con.is_connected():
        db_info = con.get_server_info()
        print('Conectado', db_info)

    update_cliente = " UPDATE users SET name = %s, email = %s WHERE  id = %s "
    val = (name, email, user_id)

    cursor2 = con.cursor()
    cursor2.execute(update_cliente, val)
    con.commit()
    return respons_users()


@app.route("/")
def root():
    return "<h1>blabla</h1>"


app.run(debug=True)