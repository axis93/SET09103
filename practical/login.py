from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/private")
def private():
	#Test for user logged in fialed
	#so redirect to login url
	return redirect(url_for('login'))

@app.route('/login')
def login():
	return "Now we would get username & passowrd"

#default page
@app.route('/')
def hello():
	return "Hello people"


# Error handling if a page is not found - route does not exist
@app.errorhandler(404)
def page_not_found(error):
	return "Couldn't find the page you requested", 404

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
