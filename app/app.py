from flask import Flask, request
import datetime
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def post():
	# read request argument
	year = request.args.get('year')
	# find date
	date = datetime.date(int(year), 1, 1) + datetime.timedelta(256-1)
	# create string 
	strr = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
	# write json format
	form = {"errorCode": 200, "dataMessage": strr}
	js = json.dumps(form)
	return js

if __name__ == '__main__':
	#Start service if that module is the main program
	app.run(debug=False, host='0.0.0.0', port=80)

