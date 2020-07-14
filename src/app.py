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
sql_connect = mysql.connect()

@app.route('/')
def hello():
    return 'hi there'

@app.route('/cpu')
def data():
    cursor = sql_connect.cursor()
    cursor.execute(
		''' SELECT * FROM cpu_usage
			WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 7 DAY);
		''')
	return json.dumps(cursor.fetchall(), indent=4, sort_keys=True, default=str)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
