from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta' # Necesario para usar flash
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


# 1. Ruta de Inicio de Sesión (Endpoint: sesion)
@app.route('/sesion')
def sesion():
    return render_template("sesion.html", autor=AUTOR)

# 2. Ruta de Registro (Endpoint: registro_form)
# Aquí puedes redirigir a la ruta principal de registro o mostrar un mensaje.
@app.route('/registro') 
def registro_form():
    # Es más limpio redirigir a la ruta principal de registro si es GET
    return redirect(url_for('register_user'))


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
        
        
        if not nombre or not email or not contraseña:
             error = "Faltan campos obligatorios."

        
        if error is not None:
            flash(error)
            
            return render_template('sesion.html', autor=AUTOR) 
        
        
        else:
            flash("Registro exitoso. ¡Bienvenido!")
            return redirect(url_for('inicio'))

if __name__ =="__main__":
    app.run(debug=True)