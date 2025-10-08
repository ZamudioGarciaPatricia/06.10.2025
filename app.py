from flask import Flask, render_template

app = (__name__)

@app.route('/')
def index():
    return render_template('base.html')
@app.route('/animales')
def index():
    return render_template('animales.html')

@app.route('/carros')
def index():
    return render_template('base.html')

@app.route('/acerca')
def index():
    return render_template('base.html')

@app.route('/maravillas')
def index():
    return render_template('base.html')


if __name__ =="__main__":
    app.run(debug=True)