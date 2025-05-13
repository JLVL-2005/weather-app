# Importamos la biblioteca 'requests' para hacer peticiones a internet
# Esto nos permitirá obtener los datos del clima desde una página web
import requests

# Diccionario con algunos lugares del estado de Jalisco, México
# Cada lugar tiene:
# - un número identificador
# - su nombre
# - latitud y longitud, que nos sirven para ubicarlo en el mapa y pedir el clima
LUGARES = {
    1: ("Arandas", 20.7052, -102.3463),
    2: ("Tepatitlán", 20.8167, -102.7667),
    3: ("Valle de Guadalupe", 21.1500, -102.6167),
    4: ("Yahualica", 21.1833, -102.8833)
}

# Diccionario que traduce los códigos del clima (que son números) a texto comprensible
# Por ejemplo, si el sitio web nos dice que el código es 0, eso significa "Despejado"
CODIGOS_CLIMA = {
    0: "Despejado",
    1: "Mayormente despejado",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Niebla",
    51: "Llovizna ligera",
    61: "Lluvia ligera",
    63: "Lluvia moderada",
    65: "Lluvia fuerte",
    80: "Lluvias ligeras",
    81: "Lluvias moderadas",
    95: "Tormenta eléctrica"
}

# Función que se encarga de obtener el clima actual para un lugar dado
# Toma como entrada la latitud y longitud del lugar
def obtener_clima(lat, lon):
    try:
        # Construimos la URL con las coordenadas para pedir el clima actual
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        # Hacemos la petición al sitio web y esperamos respuesta
        respuesta = requests.get(url, timeout=10)

        # Convertimos la respuesta en formato JSON (parecido a un diccionario de Python)
        datos = respuesta.json()

        # Tomamos los datos de clima actual desde la respuesta
        clima = datos["current_weather"]
        temperatura = clima["temperature"]          # Temperatura actual
        codigo = clima["weathercode"]               # Código del tipo de clima
        viento = clima["windspeed"]                 # Velocidad del viento

        # Buscamos una descripción en palabras del código del clima
        descripcion = CODIGOS_CLIMA.get(codigo, "Clima desconocido")

        # Devolvemos un texto con toda la información del clima
        return f"{descripcion}, {temperatura}°C, viento: {viento} km/h"
    
    # Si ocurre algún error (como problemas de conexión), mostramos un mensaje al usuario
    except:
        return "No se pudo obtener el clima. Verifica tu conexión o intenta más tarde."

# Función que muestra el menú de lugares disponibles
def mostrar_menu():
    print("\nCLIMA EN LUGARES DE JALISCO\n")
    # Mostramos todos los lugares con su número correspondiente
    for num, (nombre, _, _) in LUGARES.items():
        print(f"{num}. {nombre}")
    # También mostramos una opción para salir
    print("5. Salir")

# Función principal que controla el flujo del programa
def main():
    while True:
        mostrar_menu()  # Mostrar el menú de lugares
        opcion = input("Elige un lugar (1-4) o 5 para salir: ")  # Pedir al usuario que elija

        if opcion == "5":
            # Si el usuario escribe 5, se despide y el programa termina
            print("Gracias por usar el programa del clima.")
            break

        # Verificamos que lo que escribió sea un número válido
        if opcion.isdigit() and int(opcion) in LUGARES:
            # Obtenemos los datos del lugar seleccionado
            nombre, lat, lon = LUGARES[int(opcion)]
            print(f"\nClima en {nombre}:")
            # Mostramos el clima usando la función obtener_clima
            print(obtener_clima(lat, lon))
        else:
            # Si el número no es válido, mostramos un mensaje de error
            print("Opción no válida. Por favor elige un número del 1 al 5.")

# Esta línea asegura que el programa solo se ejecute si se abre directamente
if __name__ == "__main__":
    main()
