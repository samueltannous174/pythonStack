from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def board0():
    return render_template('index.html', rows=8, cols=8, color1='red', color2='black')

@app.route('/<int:rows>/')
def board1(rows):
    return render_template('index.html', rows=rows, cols=8, color1='red', color2='black')


@app.route('/<int:rows>/<int:cols>/<color1>/')
def board4(rows, cols,color1):
    return render_template('index.html', rows=rows, cols=cols, color1= color1, color2='black')


@app.route('/<int:rows>/<int:cols>/')
def board(rows, cols):
    return render_template('index.html', rows=rows, cols=cols, color1='red', color2='black')


@app.route('/<int:rows>/<int:cols>/<color1>/<color2>')
def board3(rows, cols , color1, color2):
    return render_template('index.html', rows=rows, cols=cols, color1=color1, color2=color2)




def main():
    app.run(debug=True)         

if __name__ == "__main__":
    main()





