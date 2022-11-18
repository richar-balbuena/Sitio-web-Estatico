from pickle import TRUE
from flask import Flask, render_template
app = Flask(__name__)  

@app.route("/")
def inicio():
    return render_template('inicio.html')


@app.route('/photos')
def photos():
    return render_template('photos.html')


@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True) 