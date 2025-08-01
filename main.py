on_off_app = True
disp_data = {}

# while on_off_app:
#     print('''Bienvenido. Este es el menú inicial.
#           Elija el número de la siguiete lista de opciones 
          
#           1. Contestar encuesta.
#           2. Visualizar resultados. 
#           0. Apagar programa''')
    
#     option = input("Ingrese el número seleccionado ahora:")

#     match option:
#         case "1": 
#             print("Sección para contestar encuesta.")
#             option = ("Presione ENTER para continuar.")
#         case "2":
#             print("Sección para visualizar resultado.")
#             option = ("Presione ENTER para continuar.")
#         case "0":
#             print("Gracias por utilizar el programa. Recuerde siempre cuidar sus dispositivos móviles.")
#             on_off_app = False
    


######## FUNCIONES DE LECTURA Y ESCRITURA DEL ARCHIVO DATA.TXT #################
#Lectura del arvhivo:
data_R = open("data.txt", "r").read()
#Escribir archivo: 
data_A = open("data.txt", "a")

#Variables Estadisticas: 
total_regis = 0
total_lt = 0
total_updt = 0
total_score = 0
max_life = 0
min_lif= 0

#Función que recorre los registros:
def regis_scan(cb, req_brand = False, req_model = False):
    #Declaración de variables:
    option = 0
    brand = ""
    model = ""
    life_time = ""
    updates = ""
    score = ""

    for char in data_R:
        if char == "|":
            
            if req_brand:
                cb(brand, model, life_time, updates, score, req_brand)
            elif req_model:
                cb(brand, model, life_time, updates, score, req_model)
            else: cb(brand, model, life_time, updates, score)

            option = 0
            brand = ""
            model = ""
            life_time = ""
            updates = ""
            score = ""
            continue

        if char == "-":
            option +=1
            continue

        match option: 
            case 0: brand += char
            case 1: model += char
            case 2: life_time += char
            case 3: updates += char
            case 4: score += char

    if req_brand:
        print(f"##### Estadísticas de la marca requerida: {req_brand}. #####")
        print(f"Promedio de vida útil en años: {(total_lt / total_regis):.2f}")
        print(f"Promedio de cantidad de actualizaciones: {(total_updt / total_regis):.2f}")
        print("Cuantas menos actualizaciones, mejor rendimiento de dispositivo.")
        print(f"Promedio de calificaciones de la marca: {(total_score / total_regis):.2f}")
        print(f"Datos calculados a partir de {total_regis} registros guardados.")

#Función para agregar un registro:
#El registro que recibe esta función cumple el siguiente formaro: 
#    "marca-modelo-años_de_vida-actualizaciones-puntaje"
def add_regis(regis):
    data_A.write(f"{regis}|")
    print("Un nuevo registro fue creado exitósamente.")
    print(f"Registro: {regis}")

#Descomentar para probar la función:
#add_regis("Apple-iPhone 12-4-6-3")

#Función cb para buscar información por marca:
def data_by_brand(brand, model, life_time, updates, score, req_brand):
    if brand.lower() == req_brand.lower():
        global total_regis 
        global total_lt
        global total_updt
        global total_score

        total_regis += 1
        total_lt += int(life_time)
        total_updt += int(updates)
        total_score += int(score)



#Función cb para mostrar todos los registros: 
def show_regis(brand, model, life_time, updates, score):
     print(f"Marca: {brand} | Modelo: {model} | Años de funcionamiento: {life_time} | Cantidad de actualizaciones: {updates} | Puntaje: {score}")

#Descomentar para probrar la función
regis_scan(show_regis) 