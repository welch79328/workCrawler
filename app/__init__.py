from crawler import Crawler
from flask import Flask, request, abort, jsonify, render_template


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():

	data = []

	if request.method == 'POST':

		post = {
			"keywords":request.form.get('keywords'),
			"area":request.form.get('area'),
			"salary":request.form.get('salary')
		}

		crawler = Crawler(post)

		data = crawler.getWorkData()


	return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)