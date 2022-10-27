from bottle import route, run, post, request, HTTPResponse
import time
import urllib
from datetime import datetime
#import logger

#configFile = "data/testwork.conf"

outfile = "data/testwork.log"

@route('/hello')
def helloPage():
	return "Hello page"

@post('/user')
def user_post():
	name = ""
	data = request.body.read().decode('utf-8')
	try:
		for kv in data.split(","):
			kvl = kv.split("=")
			if kvl[0] == "name":
				name = kvl[1]
		if name == "":
			return HTTPResponse(status=400, body="no name specified")
		with open(outfile,"a") as f:
			f.write(f"{name}: {datetime.now().strftime('%H:%M:%S %d.%m.%Y')}\n")
	except Exception as e:
		return HTTPResponse(status=500, body=str(e))
	return f"parsed: {name}"

if __name__ == '__main__':
#	logging.config.fileConfig(configFile)
#	logger = logging.getLogger("testwork")
	run(host='0.0.0.0', port=80, debug=True)
	
