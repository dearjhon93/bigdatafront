from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app,resources={r"/*/*":{"origins":"*"},})
@app.route('/consulta1/<string:year>/')
def consulta1(year: str):
  path="csvsprocesados/consulta1_hasta"+year+"join.csv"
  print(path)
  data = pd.read_csv(path)
  data = data.to_dict('records')
  return jsonify(data)

@app.route('/consulta2/<string:year>/')
def consulta2(year: str):
  path="csvsprocesados/consulta2_hasta"+year+"join.csv"
  print(path)
  data = pd.read_csv(path)
  data = data.to_dict('records')
  return jsonify(data)

@app.route('/consulta3/<string:year>/')
def consulta3(year: str):
  path="csvsprocesados/consulta3_hasta"+year+"join.csv"
  print(path)
  data = pd.read_csv(path)
  data = data.to_dict('records')
  return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
