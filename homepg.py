from flask import Flask, render_template

homepg = Flask(__name__)

@homepg.route('/')
def index():
	return render_template('index.html')
	
if __name__ == "__main__":
	homepg.rum(debug=True)
	