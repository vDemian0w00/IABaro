import random
import openpyxl

# Banco de palabras para generar nombres de gastos_hormiga
palabras_hormiga = ['cafe para llevar', 'starbuck', 'cafe de cafeteria', 'bebidas energéticas', 'monster', 'red bull', 'bebidas energetizantes','chicles', 'caja de chicles', 'paletas', 'paleta', 'papas', 'botana', 'helado', 'cerveza', 'ropa para mascota', 'vodka', 'barcadi', 'bacardi', 'don julio', 'absolute vodka', 'six chelas', 'six pack', 'bacardi', 'refresco', 'cigarro', 'cajetilla de cigarros', 'cigarros', 'malboro', 'pan dulce', 'maquillaje de lujo', 'productos de limpieza', 'dulces del metro', 'plumones', 'dulces', 'dulce', 'gomitas', 'chocolate', 'producto de belleza', 'caramelo', 'cupcakes', 'postres', 'postre', 'revistas', 'velas', 'comida mcdonalds', 'comida rápida', 'cargador de celular', 'uber', 'didi', 'ropa innecesaria', 'apuestas', 'casino', 'juegos de azar', 'pérdida de objeto personal', 'joyeria costosa', 'rolex', 'ropa de marca', 'souvenir', 'objeto de recuerdo', 'arte costoso', 'pornografia', 'pornhub premium', 'porno', 'membresia tinder', 'membresia pornhub', 'loteria', 'billete de loteria', 'productos innecesarios de amazon', 'videojuegos', 'compras innecesarias de aplicaciones móviles', 'compra impulsiva', 'chichero', 'putero', 'protitutas', 'apuesta', 'funko', 'funko', 'lego', 'figuras', 'juguete de coleccion', 'estampas', 'coleccionables', 'cuarzo', 'caja de chicles', 'chicles', 'café de la mañana', 'café de tienda', 'starbucks', 'cajetilla de cigarros', 'cigarros', 'cigarillos', 'impulsivas', 'compras impulsivas', 'miniso', 'compras de miniso', 'bebidas', 'bebida', 'vaso de café', 'comida rápida', 'mcdonald', 'mcdonalds', 'burguer king', 'snacks', 'golosinas', 'papas', 'papas fritas', 'fritos', 'takis', 'doritos', 'sabritas', 'chetos', 'chettos', 'bombones', 'bombones con chocolate', 'chocolates', 'chocolate', 'galletas maria', 'marias', 'oreo', 'ruffles', 'rufles', 'paketaxo', 'paquetaxos', 'rancheritos', 'crujitos', 'chips', 'sabritas', 'esquites', 'esquite', 'doriesquites', 'doriesquite', 'paleta', 'tutsi', 'paleta payaso', 'chamoyada', 'chicharrones', 'mazapán', 'mazapan', 'pepitas', 'pepita', 'tamales', 'tamal', 'maguitos enchilados', 'churritos de maíz', 'churros', 'churritos', 'pan dulce', 'conchas', 'pan', 'panes', 'pastillas de menta', 'halls', 'pastelitos', 'cup cakes', 'mini cup cakes', 'cacahuates', 'cacahuates japoneses', 'fruta seca', 'alfajores', 'alfajor', 'tamarindo', 'pulpa de tamarindo', 'bebida energizante', 'monster', 'rockstar', 'amper', 'monster energy', 'energy drink', 'vive 100', 'vive cien', 'corona', 'coronita', 'heineken', 'six de chelas', 'six chelero', 'modelo', 'guiness', 'guinness', 'stella artois', 'tectate', 'fria', 'helodia', 'sol', 'cerveza sol', 'bohemia', 'budweiser', 'coors', 'cerveza pacifico', 'miller', 'cervza miller', 'victoria', 'cerveza victoria', 'ritz', 'rollos de canela', 'polvorones', 'dulce', 'dulces', 'café diario', 'cafe diario', 'refresco', 'refrescos', 'coca', 'mota', 'marihuana', 'churro de mota', 'THC', 'gomitas con mota', 'mota', 'McDonalds', 'comida a domicilio', 'rappi', 'compra de rappi', 'comida rappi', 'coca', 'coca-cola', 'coca cola', 'sprite', 'squirt', 'manzanita', 'hamburguesa mcdonalds', 'hamburguesa carls jr', 'carls jr', 'hamburguesa burguer king', 'boleada zapatos', 'boleada', 'periodico', 'periodicos', 'revista', 'revistas', 'tabaco', 'alcohol', 'botella de alcohol', 'máquina expendedora', 'máquina de apuesta', 'maquina de apuesta', 'máquina expendedora', 'maquina tragamonedas', 'máquina tragamonedas', 'té helado', 'te frio', 'te helado', 'té de tienda', 'te de cafeteria', 'café de cafetería', 'bocadillo', 'caramelo', 'agua embotellada', 'torta de la calle', 'tacos de la calle', 'comida de calle', 'comida de la calle', 'tacos', 'taco', 'tortas', 'tortas', 'tacos al pastor', 'hot dogs', 'perros calientes', 'empanadas', 'empanada', '']  

# Meses
dias=['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

nombres=['ana', 'maria', 'sofia', 'isabella', 'valeria', 'lucia', 'paola', 'carolina', 'andrea', 'juliana', 'valentina', 'daniela', 'natalia', 'adriana', 'angela', 'laura', 'claudia', 'monica', 'camila', 'catalina', 'liliana', 'veronica', 'diana', 'silvia', 'patricia', 'viviana', 'johana', 'ximena', 'ana maria', 'mariana', 'paulina', 'karina', 'jessica', 'alejandra', 'cristina', 'rosa', 'jennifer', 'mary', 'jenny', 'doris', 'gabriela', 'cecilia', 'veronica', 'jimena', 'tania', 'fernanda', 'margarita', 'fabiola', 'luz',  'juan', 'carlos', 'jose', 'luis', 'miguel',  'hijo', 'hija', 'hijos', 'marido', 'esposa', 'novia', 'novio', 'tio', 'tia', 'niños', 'niña', 'niña', 'abuelita', 'abuela', 'abuelo', 'suegro', 'suegra', 'yerno', 'nuera', 'hermanastro', 'hermanastra', 'papa', 'mama', 'madre', 'padre', 'padrastro', 'madrastra', 'bisabuela', 'cuñado', 'cuñada','abuelito', 'yerno', 'sobrino', 'sobrina', 'cuñado', 'cuñada', 'Juan', 'José', 'Antonio', 'Jesús', 'Francisco', 'Manuel', 'Miguel', 'David', 'Pedro', 'Carlos', 'Daniel', 'Luis', 'Rafael', 'Alejandro', 'Roberto', 'Jorge', 'Fernando', 'Javier', 'Enrique', 'Alberto', 'Ricardo', 'Guillermo', 'Héctor', 'Mario', 'Ernesto', 'Ignacio', 'Eduardo', 'Gabriel', 'Andrés', 'Arturo', 'Armando', 'Sergio', 'Salvador', 'Oscar', 'Israel', 'Emilio', 'Juan Carlos', 'Adrián', 'Gustavo', 'Víctor', 'Raúl', 'Leonardo', 'César', 'Julio', 'Benjamín', 'José Luis', 'Ismael', 'Samuel', 'Mauricio', 'Mariano', 'Agustín', 'Gerardo', 'Abraham', 'Albert', 'Octavio', 'Alfredo', 'Joel', 'Joaquín', 'Diego', 'Jairo', 'Alonso']

# Banco de palabras para generar nombres de gastos_hormiga
nombres_hormiga=[
    'Gasto {palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    '{palabra}',
    'Pago de {palabra}',
    'Gasto de {palabra}',
    'Pago {palabra}',
    '{palabra} {nombre}',
    '{palabra} {nombre} {dia}',
    '{palabra} {dia}',
]

# Banco de frases para generar descripciones de gastos hormiga
descripciones_hormiga = [
    'Compra de {palabra}',
    'Compra de {palabra} para fiesta',
    'Pago de {palabra} para fiesta',
    'Gasto de {palabra} para fiesta',
    '{palabra} para el dia {dia}',
    '{palabra} para divertirme un rato y pasarla cool en la fiesta',
    'Gasto correspondiente a la compra de {palabra}',
    'Compra de {palabra} para {nombre}',
    'Esta compra de {palabra} es para {nombre}',
    'Regalo de {palabra}',
    'Regalo de {palabra} para {nombre}',
    'Regalo {palabra} para el dia {dia}',
    'Regalo {palabra} para el dia {dia} para {nombre}',
    'Regalo {palabra}',
]

# abrir el archivo xlsx
libro = openpyxl.load_workbook('data_synthetic_baro.xlsx')

# crear hoja de trabajo
hoja5 = libro.create_sheet("hormiga")

# escribir datos en las hojas
hoja5['A1'] = "name"
hoja5['B1'] = "description"
hoja5['C1'] = "amount"

for i in range(10000):
    name=random.choice(nombres_hormiga)
    palabra = random.choice(palabras_hormiga)
    name=name.replace('{palabra}', palabra)
    name=name.replace('{nombre}', random.choice(nombres))
    name=name.replace('{dia}', random.choice(dias))
    # establecer el contenido de la celda
    celda = 'A{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja5[celda] = name
    
    # generar la descripción
    palabra_encontrada = False
    while not palabra_encontrada:
        description=random.choice(descripciones_hormiga)
        descripcion_palabra = random.choice(palabras_hormiga)
        description=description.replace('{palabra}', descripcion_palabra)
        description=description.replace('{nombre}', random.choice(nombres))
        description=description.replace('{dia}', random.choice(dias))
        if palabra in description:
            palabra_encontrada = True
        # establecer el contenido de la celda
        celda = 'B{}'.format(i+2)  # aumentar el índice de fila para cada iteración
        hoja5[celda] = description
    
    amount=random.randint(100, 10000)
    # establecer el contenido de la celda
    celda = 'C{}'.format(i+2)  # aumentar el índice de fila para cada iteración
    hoja5[celda] = amount

# Guardar el archivo xlsx
libro.save('data_synthetic_baro.xlsx')