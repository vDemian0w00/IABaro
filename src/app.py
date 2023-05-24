from flask import Flask
from flask import jsonify
from config import config
from db.db import config_db
import json
from datetime import datetime

import requests
import numpy as np

# IMPORTS CLASSIFICATION
import json
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
#############################################################

# IMPORTS PREDICTION
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
#############################################################

# url='https://services-baro.up.railway.app/api/ia/getAllDiarios'
# url='https://services-baro.up.railway.app/api/ia/getAllFreq'

# HOLA 

# Guardar el server dentro de app
app=Flask(__name__) 
app.config['JSON_AS_ASCII'] = False # Para que no se muestren los caracteres con codificación ASCII

# Conexión BD
conn = config_db(app)

# Clasificación gastos
@app.route('/classification', methods=['GET','POST'])
def classification():
    # Obtener los gastos
    url_diarios='https://services-baro.up.railway.app/api/ia/getAllDiarios'
    url_frecuentes='https://services-baro.up.railway.app/api/ia/getAllFreq'
    # data
    data_diarios = requests.get(url_diarios)
    data_frecuentes = requests.get(url_frecuentes)
    # Convertir datos


    # CLASIFICACIÓN
    # Clases
    class Classification_GD:
        FIJOS_IMP="FRECUENTE_IMPRESCINDIBLE" # Servicios que se pagan en un periodo de tiempo frecuente y la cantidad es siempre igual o llega a variar muy poco (NECESARIOS)
        FIJOS_PRE="FRECUENTE_PRESCINDIBLE" # Servicios que se pagan en un periodo de tiempo frecuente y la cantidad es siempre igual o llega a variar muy poco (PUEDEN EVITARSE)
        VARIABLES_IMP="VARIABLE_IMPRESCINDIBLE" # Subcategoria de gasto diario (NECESARIOS)
        VARIABLES_PRE="VARIABLE_PRESCINDIBLE" # Subcategoria de gasto diario (PUEDEN EVITARSE)
        HORMIGA="HORMIGA" # Gastos pequeños que se realizan cada día y que suman mucho al final del mes
        IMPREVISTOS="IMPREVISTO" # Gastos que no se pueden prever y que se realizan en un momento dado

    class Review:
        def __init__(self, name, description, classification):
            self.name=name
            self.description=description
            self.classification=classification

    class ReviewContainer:
        def __init__(self, reviews):
            self.reviews = reviews
        
        def get_dataSet(self):
            return [f'{x.name} - {x.description}' for x in self.reviews]
        
        def get_x(self, vectorizer):
            data_vector = vectorizer.transform(self.get_dataSet())
            return data_vector
        
        def get_y(self):
            return [x.classification for x in self.reviews]

    # Leer los datos de entrenamiento de los archivos json
    file_names = ['data_classification/fijos_imp.json', 'data_classification/fijos_pre.json','data_classification/diarios_imp.json', 'data_classification/diarios_pre.json', 'data_classification/hormiga.json', 'data_classification/imprevistos.json']
    file_categories = [Classification_GD.FIJOS_IMP, Classification_GD.FIJOS_PRE, Classification_GD.VARIABLES_IMP, Classification_GD.VARIABLES_PRE, Classification_GD.HORMIGA, Classification_GD.IMPREVISTOS]

    reviews = []
    for i in range(len(file_names)):
        file_name = file_names[i]
        classification = file_categories[i]
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.read()
            review_json = json.loads(data)
            for review_from_json in review_json:
                review = Review(review_from_json['name'], review_from_json['description'], classification)
                reviews.append(review)

    # Preparar los datos para la clasificacion
    train, test=train_test_split(reviews, test_size=0.4, random_state=42) # CAMBIO DEL PORCENTAJE DE LOS DATOS DE TESTEO
    train_container=ReviewContainer(train)
    test_container = ReviewContainer(test)

    # Vectorizacion de datos
    corpus = train_container.get_dataSet()
    vectorizer = TfidfVectorizer()
    vectorizer.fit(corpus)

    # Entrenamiento de datos
    train_x = train_container.get_x(vectorizer)
    train_y = train_container.get_y()

    test_x = test_container.get_x(vectorizer)
    test_y = test_container.get_y()

    # Clasificacion
    clf = svm.SVC(C=16, kernel='linear', gamma='auto')
    clf.fit(train_x, train_y)

    test_set = ['agua', 'funeral', 'muerte', 'café de la tienda']
    new_test = vectorizer.transform(test_set)

    print(clf.predict(new_test))

    # Performance
    y_pred = clf.predict(test_x)
    f1_score(test_y, y_pred, average=None)
    print(clf.score(test_x, test_y))

    respuesta={'Clasificacions de gastos': clf.predict(new_test)}    
    return jsonify(respuesta)

# Predicciones gastos
@app.route('/prediction', methods=['GET','POST'])
def prediction():
    # Obtener los gastos
    url_diarios='https://services-baro.up.railway.app/api/ia/getAllDiarios'
    url_frecuentes='https://services-baro.up.railway.app/api/ia/getAllFreq'
    # data
    data_diarios = requests.get(url_diarios)
    data_frecuentes = requests.get(url_frecuentes)
    
    # Dataframe
    df=pd.read_csv('PRUEBA.csv')

# Data
@app.route('/data_gastos', methods=['GET'])
def getDataGastos():
    # Obtener los gastos
    url_diarios='https://services-baro.up.railway.app/api/ia/getAllDiarios'
    url_frecuentes='https://services-baro.up.railway.app/api/ia/getAllFreq'
    # data
    data_diarios = requests.get(url_diarios)
    data_frecuentes = requests.get(url_frecuentes)
    
    return jsonify({'data_diarios': data_diarios.json(), 'data_frecuentes': data_frecuentes.json()})

# # Ruta para obtener los gastos diarios
# @app.route('/gasto_diario')
# def getGastoDiario():
#     cur = conn.connection.cursor()
#     cur.execute("SELECT * FROM diarios")
#     gasto_diario = cur.fetchall()

#     lista_gastos = []
#     for gasto in gasto_diario:
#         dict_gasto = {
#             'id': gasto[0],
#             'nombre': gasto[1],
#             'descripcion': gasto[2],
#             'monto': gasto[3],
#             'icon': gasto[4],
#             'dayId': gasto[5]
#         }
#         lista_gastos.append(dict_gasto)
    
#     # Nombre del archivo json
#     data_diarios = "./classification/gastos-diarios.json"

#     # Abre el archivo en modo de lectura y escritura
#     with open(data_diarios, 'r+') as archivo_json:
#         # Intenta cargar los datos existentes del archivo JSON
#         try:
#             datos_existentes = json.load(archivo_json)
#         except json.decoder.JSONDecodeError:
#             datos_existentes = []

#         nuevos_datos = []

#         # Agrega los nuevos datos a la lista de nuevos datos si no existen en los datos existentes
#         for gasto in lista_gastos:
#             if gasto not in datos_existentes:
#                 nuevos_datos.append(gasto)

#         # Elimina los datos existentes que no están en la lista de gastos de la base de datos
#         datos_actualizados = [dato for dato in datos_existentes if dato in lista_gastos]

#         # Agrega los nuevos datos a los datos actualizados
#         datos_actualizados += nuevos_datos

#         # Rebobina el archivo al principio para sobrescribir los datos antiguos
#         archivo_json.seek(0)

#         # Escribe los datos actualizados en el archivo JSON
#         json.dump(datos_actualizados, archivo_json, indent=4)

#         # Elimina los datos existentes que no están presentes en la lista de gastos de la base de datos
#         archivo_json.truncate()

#     # Devuelve los datos actualizados en formato JSON
#     return json.dumps(datos_actualizados, indent=4)

# #Ruta para obtener los gastos frecuentes
# @app.route('/gasto_frecuente')
# def getGastoFrecuente():
#     cur = conn.connection.cursor()
#     cur.execute("SELECT * FROM frecuentes")
#     gasto_diario = cur.fetchall()
    
#     lista_gastos = []
#     for gasto in gasto_diario:
#         dict_gasto = {
#             'id': gasto[0],
#             'nombre': gasto[1],
#             'descripcion': gasto[2],
#             'monto': gasto[3],
#             'icon': gasto[4],
#             'dayId': gasto[5]
#         }
#         lista_gastos.append(dict_gasto)
    
#     # Nombre del archivo json
#     data_frecuentes = "./classification/gastos-frecuentes.json"
    
#     # Abre el archivo en modo de lectura y escritura
#     with open(data_frecuentes, 'r+') as archivo_json:
#         # Intenta cargar los datos existentes del archivo JSON
#         try:
#             datos_existentes = json.load(archivo_json)
#         except json.decoder.JSONDecodeError:
#             datos_existentes = []

#         nuevos_datos = []

#         # Agrega los nuevos datos a la lista de nuevos datos si no existen en los datos existentes
#         for gasto in lista_gastos:
#             if gasto not in datos_existentes:
#                 nuevos_datos.append(gasto)

#         # Elimina los datos existentes que no están en la lista de gastos de la base de datos
#         datos_actualizados = [dato for dato in datos_existentes if dato in lista_gastos]

#         # Agrega los nuevos datos a los datos actualizados
#         datos_actualizados += nuevos_datos

#         # Rebobina el archivo al principio para sobrescribir los datos antiguos
#         archivo_json.seek(0)

#         # Escribe los datos actualizados en el archivo JSON
#         json.dump(datos_actualizados, archivo_json, indent=4)

#         # Elimina los datos existentes que no están presentes en la lista de gastos de la base de datos
#         archivo_json.truncate()

#     # Devuelve los datos actualizados en formato JSON
#     return json.dumps(datos_actualizados, indent=4)


# Run
if(__name__ == '__main__'):
    app.config.from_object(config['development'])
    app.run(port=config['development'].PORT)