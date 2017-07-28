
#~Author: 
#~Description:
#~AppName: {}


from flask import Flask

#instantiate Flask
app= Flask(__name__)

@app.route("/")
def hello():
	return "<b> My {} app </b>"


if __name__=='__main__':
	app.run(debug=True)


