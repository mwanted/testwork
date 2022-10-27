from bottle import route, run, post, request, HTTPResponse
import time
import urllib
from datetime import datetime
#import logger
import sqlite3
import os

#configFile = "data/testwork.conf"

outfile = "data/testwork.log"
outdb = "data/testwork.db"

def write_data(name):
	if databackend == "sqlite":
		try:
			cursor = sqlite_connection.cursor()
			sqlite_query = f"INSERT INTO USERLOG (username,timestamp) VALUES (\"{name}\",{int(time.time())});"
			cursor.execute(sqlite_query)
			sqlite_connection.commit()
			cursor.close()
		except sqlite3.Error as error:
			return HTTPResponse(status=500, body="SQLite error: {str(error)}")
	else:
		with open(outfile,"a") as f:
			f.write(f"{name}: {datetime.now().strftime('%H:%M:%S %d.%m.%Y')}\n")

@route('/hello')
def helloPage():
	return "Hello page"

@route('/user')
def user_get():
	if databackend != "sqlite":
		return HTTPResponse(status=500, body="Wrong backend")
	name = request.query.name
	try:
		cursor = sqlite_connection.cursor()
		sqlite_query = f"SELECT timestamp FROM USERLOG WHERE username=\"{name}\";"
		cursor.execute(sqlite_query)
		record = cursor.fetchall()
	except sqlite3.Error as error:
		return HTTPResponse(status=500, body="SQLite error: {str(error)}")
	ans = list()
	for timetouple in record:
		timestamp, = timetouple
		ans.append(f"{name}: {datetime.fromtimestamp(int(timestamp)).strftime('%H:%M:%S %d.%m.%Y')}")
	return "\n".join(ans)

@post('/user')
def user_post():
	name = ""
	data = request.body.read().decode()
	try:
		for kv in data.split(","):
			kvl = kv.split("=")
			if kvl[0] == "name":
				name = kvl[1]
		if name == "":
			return HTTPResponse(status=400, body="no name specified")
		write_data(name)
	except Exception as e:
		return HTTPResponse(status=500, body=str(e))
	return f"parsed: {name}"

def db_connect(db):
	try:
		sqlite_connection = sqlite3.connect(db)
		cursor = sqlite_connection.cursor()
		sqlite_query = "CREATE TABLE IF NOT EXISTS USERLOG (username TEXT, timestamp INTEGER);"
		cursor.execute(sqlite_query)
	except sqlite3.Error as error:
		print("SQLite commection error: ", error)
		exit()
	return sqlite_connection
		

if __name__ == '__main__':
#	logging.config.fileConfig(configFile)
#	logger = logging.getLogger("testwork")
	databackend = os.environ['DATABACKEND']
	if databackend == "sqlite":
		sqlite_connection = db_connect(outdb)
	run(host='0.0.0.0', port=8088, debug=True)
	
