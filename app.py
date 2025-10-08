from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    autor = 'Zamudio Garcia Patricia'
    return render_template('inicio.html', autor=autor)


@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/carros')
def carros():
    return render_template('base.html')

@app.route('/acerca')
def acerca():
    return render_template('base.html')

@app.route('/maravillas')
def maravillas():
    return render_template('base.html')


if __name__ =="__main__":
    app.run(debug=True)