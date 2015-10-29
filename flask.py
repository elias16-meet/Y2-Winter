from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/Hello/', methods=['POST'])
@app.route('/Hello/<name>')
def Hello():
	a = request.form['name']
	return render_template('Hello.html', name=a)

if __name__ == "__main__": 
	app.run() 