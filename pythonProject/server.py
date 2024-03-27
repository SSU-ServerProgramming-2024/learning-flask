from flask import Flask
import random

app = Flask(__name__)

topics = [
	{'id': 1, 'title': 'html', 'body': 'html is ...'},
	{'id': 2, 'title': 'css', 'body': 'css is ...'},
	{'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

@app.route('/')  #사용자가 path를 입력하지 않고 접속하면 밑에 있는 함수가 응대해라
def index():
	liTags =''
	for topic in topics:
		liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</li>'
	return f'''<!doctype html>
	<html>
		<body>
			<h1><a href="/">WEB</a></h1>
			<ol>
				{liTags}
			</ol>
			<h2>Welcome</h2>
			Hello, Web
		</body>
	</html>
	'''

@app.route('/create/')
def create():
	return 'Create'

@app.route('/read/<id>/')
def read(id):
	print(id)
	return 'Read ' + id

app.run(debug=True)