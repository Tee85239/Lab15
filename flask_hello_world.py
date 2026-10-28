# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
# route decorator binds a function to a URL
bootstrap = Bootstrap5(app)
@app.route('/')

@app.route('/mytemplate')
def t_test():
    return render_template('my_template_1.html', message='Hello from Flask!')

def hello():
    return 'Hello world from Flask!'