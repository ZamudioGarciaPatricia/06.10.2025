from flask import Flask, render_template, request, redirect, url_for, flash 

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
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
    return render_template("sesion.html", autor=AUTOR)


@app.route('/registro') 
def registro_form():
    
    return redirect ('/sesion.html')


@app.route('/registrandome', methods= ('GET', 'POST'))
def register_user():

    if request.method == 'POST':
        error = None
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        contraseña = request.form.get('contraseña')
        conficont = request.form.get('conficont')
        mes = request.form.get('mes')
        dias = request.form.get('Dias')
        añonac = request.form.get('añonac')
        genero = request.form.get('genero')


        if contraseña != conficont:
            error = "Las contraseñas no coinciden, intenta de nuevo."

        
        if error is not None:
            flash(error)
            
            return render_template('sesion.html', autor=AUTOR) 
        
        
        else:
            flash("Registro exitoso. ¡Bienvenido!")
            return redirect(url_for('inicio'))
        
        
        

if __name__ =="__main__":
    app.run(debug=True)