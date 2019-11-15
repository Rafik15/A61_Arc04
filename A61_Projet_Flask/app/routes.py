from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    modeles = {'titre': 'Regression Lineaire'}
    parametres = [
        {"par1":"10" , "par2":"uniforme" },
        {"par1" : "20" ,  "par2" : "lineaire"}
    ]
    return render_template('index.html', title = 'Accueil', mod = modeles, page_no=1, param = parametres)

from app.forms import ModelePredictionForm
from flask import flash, redirect

@app.route('/form_input', methods=['GET', 'POST'])
def form_input():
    form=ModelePredictionForm()
    if form.validate_on_submit():
        flash('Nom:{}, Age:{}'.format(
            form.nom.data, form.age.data
        ))
        return redirect('/index')
    return render_template('form_input.html', title='Modele de Prediction', form=form)
#<html>
  #  <head>
  #      <title>Accueil – Utilisation de RL</title>
  #  </head>
  #  <body>
  #      <h1>Utilisation du modele : ''' + modeles['titre'] + '''!</h1>
   # </body>
#</html>
