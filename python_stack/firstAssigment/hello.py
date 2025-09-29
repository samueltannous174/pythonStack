from flask import Flask  

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Champion')
def champion():
    return 'Champion!'

@app.route('/say/<name>')
def say(name):
    return f'Hi {name}!'

@app.route('/repeat/<count>/<word>')
def repeat(count, word):
    return (word + ' ')*int(count)


if __name__ == '__main__':
    app.run(debug=True)