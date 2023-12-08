from flask import Flask,render_template,redirect,url_for,request	
from data_processing import class_count_percentage
app = Flask(__name__)
	

@app.route('/')
def index(value=class_count_percentage):
	return render_template('index.html',value=class_count_percentage)

if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0")