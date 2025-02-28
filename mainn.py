# Importamos Flask y la función render_template para usar plantillas HTML con Jinja
from flask import Flask, render_template

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Función para calcular el consumo energético
def result_calculate(size, lights, device):
    # Coeficientes para calcular el consumo de energía
    home_coef = 100  # Cada metro cuadrado consume 100 unidades de energía
    light_coef = 0.04  # Cada luz consume 0.04 unidades de energía
    devices_coef = 5  # Cada dispositivo electrónico consume 5 unidades de energía
    
    # Retornamos el cálculo basado en las variables recibidas
    return size * home_coef + lights * light_coef + device * devices_coef 

# Ruta de la página principal
@app.route('/')
def index():
    # Renderiza la plantilla index.html
    return render_template('index.html')

# Ruta donde el usuario ingresa el tamaño de la casa
@app.route('/<size>')
def lights(size):
    # Renderiza lights.html y pasa la variable size a la plantilla
    return render_template('lights.html', size=size)

# Ruta donde el usuario ingresa el número de luces
@app.route('/<size>/<lights>')
def electronics(size, lights):
    # Renderiza electronics.html y pasa las variables size y lights a la plantilla
    return render_template('electronics.html', size=size, lights=lights)

# Ruta donde el usuario ingresa la cantidad de dispositivos electrónicos
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    # Calcula el consumo energético con la función result_calculate
    # Renderiza end.html y pasa el resultado del cálculo como variable result
    return render_template('end.html', result=result_calculate(int(size), int(lights), int(device)))

# Ejecutamos la aplicación en modo debug para facilitar la detección de errores
app.run(debug=True)
