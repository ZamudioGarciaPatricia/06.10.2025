from flask import Flask, render_template

app = Flask(__name__)
AUTOR = "patricia Zamudio Garcia"

@app.route('/')
def inicio():
    return render_template('inicio.html', autor=AUTOR)

@app.route('/animales') 
def animales():
    return render_template('animales.html', autor=AUTOR) 

@app.route('/carros') 
def carros():
    return render_template('carros.html', autor=AUTOR)

@app.route('/maravillas') 
def maravillas():
    return render_template('maravillas.html', autor=AUTOR)

@app.route('/acerca') 
def acerca_de():
    return render_template('acerca.html', autor=AUTOR)


@app.route('/sesion') 
def sesion():
    return render_template('sesion.html', autor=AUTOR)

if __name__ =="__main__":
    app.run(debug=True)