from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/men/<username>')
def show_man_profile(username):
    print username
    return render_template("user.html")

@app.route('/route/with/<vararg>')
def handler_function(vararg):
  print vararg
  return render_template("user.html")

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
	print username
	print id
	return render_template("user.html")

app.run(debug=True)


