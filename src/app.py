from flask import Flask
from flaskext.mysql import MySQL
import os, json, subprocess, yaml

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ[ 'MYSQL_USER' ]
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ[ 'MYSQL_PASSWORD' ]
app.config['MYSQL_DATABASE_DB'] = os.environ[ 'MYSQL_DATABASE' ]
app.config['MYSQL_DATABASE_HOST'] = os.environ[ 'MYSQL_HOST' ]

mysql.init_app(app)

@app.route('/cpu')
def cpu():
	cursor = mysql.connect().cursor()
	cursor.execute('''
				SELECT * FROM cpu_usage
				WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 7 DAY);
				''')
	result = list(cursor.fetchall())
	result = [{'usage': usage, 'taken_at': taken_at} for usage, taken_at in result]
	return json.dumps(result, indent=4, sort_keys=True, default=str)

@app.route('/cpu_average')
def cpu_average():
	cursor = mysql.connect().cursor()
	cursor.execute(''' SELECT avg(`usage`) FROM `cpu_usage`; ''')
	result = { 'cpu_avg_usage': float(cursor.fetchone()[0]) }
	return json.dumps(result, indent=4, sort_keys=True, default=str)

@app.route('/memory')
def memory():
	cursor = mysql.connect().cursor()
	cursor.execute('''
				SELECT * FROM mem_usage
				WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 7 DAY);
				''')
	result = list(cursor.fetchall())
	result = [{'used_space': used, 'free_space': free, 'taken_at': taken_at} for used, free, taken_at in result]
	return json.dumps(result, indent=4, sort_keys=True, default=str)

@app.route('/memory_average')
def memory_average():
	cursor = mysql.connect().cursor()
	cursor.execute('''SELECT avg(`used`), avg(`free`) FROM `mem_usage`; ''')
	result = cursor.fetchone()
	result = { 'memory_avg_used_space': float(result[0]), 'memory_avg_free_space': float(result[1]) }
	return json.dumps(result, indent=4, sort_keys=True, default=str)

@app.route('/storage')
def storage():
	cursor = mysql.connect().cursor()
	cursor.execute('''
				SELECT * FROM disk_usage
				WHERE taken_at >= DATE_SUB(NOW(), INTERVAL 7 DAY);
				''')
	result = list(cursor.fetchall())
	result = [{'used_space': used, 'free_space': free, 'taken_at': taken_at} for used, free, taken_at in result]
	return json.dumps(result, indent=4, sort_keys=True, default=str)

@app.route('/storage_average')
def storage_average():
	cursor = mysql.connect().cursor()
	cursor.execute(''' SELECT avg(`used`), avg(`free`) FROM `disk_usage`; ''')
	result = list(cursor.fetchone())
	result = { 'disk_avg_used_space': float(result[0]), 'disk_avg_free_space': float(result[1]) }
	return json.dumps(result, indent=4, sort_keys=True, default=str)

@app.route('/current')
def current():
	cursor = mysql.connect().cursor()
	file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data_collector')
	file_name = 'get_current_measurements'
	measurements = subprocess.check_output(['bash', os.path.join(file_dir, file_name)])
	measurements = yaml.load(measurements)
	return json.dumps(measurements, indent=4, sort_keys=True, default=str)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
