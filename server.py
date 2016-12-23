from flask import Flask , render_template

app = Flask(__name__)

@app.errorhandler(404)
def error(e):
	return render_template('404.html'), 404

@app.route('/')
def main():
	return render_template("main.html")


@app.route('/name')
def name():
	return render_template("name.html")

@app.route('/profile')
def profile():
	return render_template("profile.html")

@app.route('/blog')
def blog():
	return render_template("blog.html")


if __name__=='__main__':
	app.run()