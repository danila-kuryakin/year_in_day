from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_query_string():
	year = request.args.get('year')
	return year

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
