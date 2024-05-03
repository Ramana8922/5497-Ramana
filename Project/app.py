from flask import Flask,render_template
app = Flask(__name__) #initialising Flask


@app.route('/')
def index():
 return render_template('index.html')

if __name__ == '_main_':
 app.run()