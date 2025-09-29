from flask import Flask, render_template
 
app = Flask(__name__)
@app.route('/play')
def hello_world():
    return render_template('index.html', number = 3)
@app.route('/play/<number>')
def hello_world2(number):
    return render_template('index.html',number = int(number))
 
@app.route('/play/<number>/<color>')
def hello_world3(number, color):
    return render_template('index.html',number = int(number), color = color)
   
 
if __name__ == "__main__":
    app.run(debug=True)