import os
import configparser
from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL, MySQLdb  # pip install flask-mysqldb

# Configuração do caminho para o arquivo .ini
userprofile = os.environ['USERPROFILE']
# file_path = os.path.join(userprofile, "credenciais")
file_path = os.path.join(userprofile, "Desktop", "Projetos", "flask-socketio", "config")
file_config = os.path.join(file_path, "hml-mysql.ini")

# Leitura do arquivo de configuração
config = configparser.ConfigParser()
config.read(file_config)

app = Flask(__name__)
app.secret_key = "datasageanalytics"

# Configurações do MySQL lidas do arquivo .ini
app.config['MYSQL_HOST'] = config['mysql']['host']
app.config['MYSQL_USER'] = config['mysql']['user']
app.config['MYSQL_PASSWORD'] = config['mysql']['password']
app.config['MYSQL_DB'] = config['mysql']['db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('progressbar.html')

@app.route("/ajaxprogressbar", methods=["POST", "GET"])
def ajaxprogressbar():
    if request.method == 'POST':
        username = request.form['username']
        useremail = request.form['useremail']
        print(username)
        cur = mysql.connection.cursor()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("INSERT INTO tbl_user (username, useremail) VALUES (%s, %s)", [username, useremail])
        mysql.connection.commit()
        cur.close()
        msg = 'New record created successfully'
    return jsonify(msg)

if __name__ == "__main__":
    app.run(debug=True)
