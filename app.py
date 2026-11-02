# importar pacotes
import flask 
from flask import Flask
import pandas as pd
import pickle
from pathlib import Path

# definir caminhos absolutos baseados na localização do próprio app.py 
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / 'model'

# importar modelo e feature names
with open(MODEL_DIR / 'modelo_simples.pkl', 'rb') as file:
    modelo = pickle.load(file)
with open(MODEL_DIR / 'features_simples.names', 'rb') as file:
    features = pickle.load(file)

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('home.html')

    if flask.request.method == 'POST':

        # dicionário contendo as informações imputadas pelo usuário
        user_inputs = {
            'Condo': flask.request.form['condominio'],
            'Size': flask.request.form['area'],
            'Rooms': flask.request.form['quartos'],
            'Suites': flask.request.form['suites']
        }

        # input para dataframe(em branco)
        df = pd.DataFrame(index=[0], columns=features)
        df = df.fillna(0)

        # percorrer o dicionário e usá-lo para imputar os valores digitados
        # pelo usuário em suas respectivas colunas dentro do dataframe
        for i in user_inputs.items():
            df[i[0]] = i[1]

        # conversão de tipo de dado para float
        df = df.astype(float)

        # fazer a previsão
        y_pred = modelo.predict(df)[0]

        y_pred = f"{y_pred:,.2f}"
        y_pred = y_pred.replace(",", "X").replace(".", ",").replace("X", ".")
        
        return flask.render_template('home.html', valor_venda=y_pred)

if __name__ == '__main__':
    app.run()