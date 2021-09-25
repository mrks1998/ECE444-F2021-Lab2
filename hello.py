from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello Mohammadreza!</h1>'
if __name__ == '__main__':
 app.run(debug=True)

 @app.route('/')
def index():
 return render_template('index.html')
@app.route('/user/<name>')
def user(name):
 return render_template('user.html', name=name)
