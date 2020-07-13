from flask import Flask
from flaskext.mysql import MySQL
import os, json

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'example'
app.config['MYSQL_DATABASE_DB'] = 'performance_api_app'
app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)

@app.route('/')
def hello():
    return 'hi there'

@app.route('/data')
def data():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from cpu_usage")
    return json.dumps(cursor.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
