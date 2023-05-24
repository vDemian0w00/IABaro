# Imports
import json
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score

# Clases
class Classification_GD:
    FIJOS_IMP="FIJOS_IMPRESCINDIBLES" # Servicios que se pagan en un periodo de tiempo frecuente y la cantidad es siempre igual o llega a variar muy poco (NECESARIOS)
    FIJOS_PRE="FIJOS_PRESCINDIBLES" # Servicios que se pagan en un periodo de tiempo frecuente y la cantidad es siempre igual o llega a variar muy poco (PUEDEN EVITARSE)
    VARIABLES_IMP="VARIABLES_IMPRESCINDIBLES" # Subcategoria de gasto diario (NECESARIOS)
    VARIABLES_PRE="VARIABLES_PRESCINDIBLES" # Subcategoria de gasto diario (PUEDEN EVITARSE)
    HORMIGA="HORMIGA" # Gastos pequeños que se realizan cada día y que suman mucho al final del mes
    IMPREVISTOS="IMPREVISTOS" # Gastos que no se pueden prever y que se realizan en un momento dado

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

# Leer los datos de los archivos json
file_names = ['./fijos_imp.json', './fijos_pre.json','./diarios_imp.json', './diarios_pre.json', './hormiga.json', './imprevistos.json']
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

# Nombres y descripciones de gastos diarios
file_gastos_diarios = "./gastos-diarios.json"
data_diarios = []

with open(file_gastos_diarios, 'r', encoding='utf-8') as json_gastos_diarios:
    dataD=json_gastos_diarios.read()
    dataD_json=json.loads(dataD)
    for gasto in dataD_json:
        data_diarios.append(f'{gasto["nombre"]}-{gasto["descripcion"]}')
    # print(data_diarios)

# Nombres y descripciones de gastos fijos
file_gastos_fijos = "./gastos-frecuentes.json"
data_fijos = []

with open(file_gastos_fijos, 'r', encoding='utf-8') as json_gastos_fijos:
    dataF=json_gastos_fijos.read()
    dataF_json=json.loads(dataF)
    for gasto in dataF_json:
        data_fijos.append(f'{gasto["nombre"]}-{gasto["descripcion"]}')
    # print(data_fijos)

# Clasificacion
clf = svm.SVC(C=16, kernel='linear', gamma='auto')
clf.fit(train_x, train_y)

test_set = ['curso pipn niños']
new_test = vectorizer.transform(test_set)

print(clf.predict(new_test))

# Performance
y_pred = clf.predict(test_x)
f1_score(test_y, y_pred, average=None)
print(clf.score(test_x, test_y))


