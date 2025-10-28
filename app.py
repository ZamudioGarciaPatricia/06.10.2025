from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta' 

AUTOR = "patricia zamudio garcia"

USUARIOS_REGISTRADOS = {
    
}

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
def acerca():
    return render_template('acerca.html', autor=AUTOR)

@app.route('/login')
def login():
    return render_template('login.html', autor=AUTOR)

@app.route('/login', methods=['POST'])
def validaLogin():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    if not email or not password:
        flash('Por favor, ingresa email y contraseña.', 'error')
        return render_template('login.html', autor=AUTOR)

    if email in USUARIOS_REGISTRADOS:
        usuario = USUARIOS_REGISTRADOS[email]
        
        if usuario['password'] == password:
            session['usuario_email'] = email
            session['usuario'] = usuario['nombre']
            session['logueado'] = True

            flash(f"Bienvenido, {usuario['nombre']}!", 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Contraseña incorrecta', 'error')
            return render_template('login.html', autor=AUTOR)
    else:
        flash('Usuario no encontrado', 'error')
        return render_template('login.html', autor=AUTOR)

@app.route("/logout")
def logout():
    session.pop('usuario_email', None)
    session.pop('usuario', None)
    session.pop('logueado', None)
    
    flash('Has cerrado sesión correctamente.', 'success')
    return redirect(url_for('inicio'))

@app.route('/registro')
def registro_form():
    return redirect(url_for('sesion'))

@app.route('/sesion')
def sesion():
    return render_template('sesion.html', autor=AUTOR)

@app.route('/registrandome', methods=['GET', 'POST'])
def register_user():
    
    if request.method == 'POST':
        error = None
        
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        contraseña = request.form.get('contraseña')
        conficont = request.form.get('conficont')
        
        mes = request.form.get('mes')
        dias = request.form.get('dias')
        añonac = request.form.get('añonac')
        genero = request.form.get('genero')

        if contraseña != conficont:
            error = "Las contraseñas no coinciden, intenta de nuevo."
        
        if email in USUARIOS_REGISTRADOS:
            error = "El email ya está registrado. Intenta iniciar sesión."
            
        if not all([nombre, apellido, email, contraseña, conficont]):
                error = "Faltan campos obligatorios por llenar."

        if error is not None:
            flash(error, 'error')
            return render_template('sesion.html', autor=AUTOR)