######      APLICACIÓN VIDA ÚTIL DE SMARTPHONES    ######

#------------------ AMBIENTE: 
#Variable para encender o apagar el programa:
on_off_app = True

#Variable para controlar el submenú:
sub_menu_activo = True
    
######## FUNCIONES DE LECTURA Y ESCRITURA DEL ARCHIVO DATA.TXT 
#Lectura del arvhivo:
data_R = open("data.txt", "r").read()

#Variables Estadisticas: 
total_regis = 0
total_lt = 0
total_updt = 0
total_score = 0

######## FUNCIONES PARA COMPLETAR LA ENCUESTA:
#Respondiente los temas "marca-modelo-años_de_vida-actualizaciones-puntaje o rendimiento general"

def encuesta():
    while True:
        try:
            marca = input("Ingrese la marca del dispositivo: ").strip()
            if marca and len(marca) >= 2:
                marca.capitalize()
                break
            else:
                print("="*50)
                print("La marca tiene que ser de almenos de 2 caracter.")
                print("="*50)
        except Exception:
            print("❌ Error al ingresar la marca. Intentelo denuevo.")
        
    while True:
        try:
            modelo = input("Ingrese el modelo del dispositivo: ").strip()
            if modelo and len(modelo) > 0:
                break
            else:
                print("="*50)
                print("Por favor ingrese denuevo el modelo.")
                print("="*50)
        except Exception:
            print("❌ Error al ingresar el modelo. Intente denuevo.")

    while True:
        try:
            tiempo_vida = input("Ingrese los años de uso que tuvo el dispositivo: ").strip()
            tiempo_vida = int(tiempo_vida)
            if 0 < tiempo_vida < 20:
                tiempo_vida = str(tiempo_vida)
                break
            else:
                print("="*50)
                print("El tiempo de uso puede tener entre 0-20 años.")
                print("="*50)
        except TypeError:
            print("❌ Error, el tipo de dato tiene que ser numerico.")
        except Exception:
            print("❌ Error al ingresar el tiempo de vida. Intentelo denuevo.")


    while True:
        try:
            actualizaciones = input("Ingrese cantidades de actualizaciones que tiene el dispositivo: ")
            actualizaciones = int(actualizaciones)
            if 0 < actualizaciones < 100:
                actualizaciones = str(actualizaciones)
                break
            else:
                print("="*50)
                print("La cantidades de actualizaciones tiene que estar entre 0-100")
                print("="*50)
        except TypeError:
            print("❌ Error, el tipo de dato tiene que ser númerico.")
        except Exception:
            print("❌ Error al ingresar la cantidad de actualizaciones. Intente denuevo.")
    
    while True:
        try:
            rendimiento = input("Ingrese el rendimiento general del dispositivo del (1-10): ")
            rendimiento = int(rendimiento)
            if 0 < rendimiento <= 10:
                rendimiento = str(rendimiento)
                break
            else:
                print("="*50)
                print("La actuacion tiene que ser entre el 1 al 10.")
                print("="*50)
        except TypeError:
            print("❌ Error, el tipo de dato tiene que ser númerico.")
        except Exception:
            print("❌ Error al ingresar la putuacion de rendimiento. Intente denuevo.")


    #Concatenamos los strings
    return (f"{marca}-{modelo}-{tiempo_vida}-{actualizaciones}-{rendimiento}")

#Función que recorre los registros:
def regis_scan(cb, req_brand = False, req_model = False):
    #Declaración de variables:
    option = 0
    brand = model = life_time = updates = score = ""

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
        print("-"*50)
        print(f"##### Estadísticas de la marca requerida: {req_brand}. #####")
        print(f"Promedio de vida útil en años: {(total_lt / total_regis):.2f}")
        print(f"Promedio de cantidad de actualizaciones: {(total_updt / total_regis):.2f}")
        print("Cuantas menos actualizaciones, mejor rendimiento de dispositivo.")
        print(f"Promedio de calificaciones de la marca: {(total_score / total_regis):.2f}")
        print(f"Datos calculados a partir de {total_regis} registros guardados.")

    if req_model:
        print("-"*50)
        print(f"##### Estadísticas del modelo requerido: {req_brand}. #####")
        print(f"Promedio de vida útil en años: {(total_lt / total_regis):.2f}")
        print(f"Promedio de cantidad de actualizaciones: {(total_updt / total_regis):.2f}")
        print("Cuantas menos actualizaciones, mejor rendimiento de dispositivo.")
        print(f"Promedio de calificaciones de la marca: {(total_score / total_regis):.2f}")
        print(f"Datos calculados a partir de {total_regis} registros guardados.")


#Función para agregar un registro:
#El registro que recibe esta función cumple el siguiente formaro: 
#    "marca-modelo-años_de_vida-actualizaciones-puntaje"
def add_regis(regis):
    #Escribir archivo: 
    data_A = open("data.txt", "a")
    data_A.write(f"{regis}|")
    data_A.close()
    print("Un nuevo registro fue creado exitósamente.")
    print(f"Registro: {regis}")
    

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

#Función cb para buscar información por modelo: 
def data_by_model(brand, model, life_time, updates, score, req_model):
    if model.lower() == req_model.lower():
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



#------------------ PROCESO:
 
#Menú de navegación de la aplicación:
while on_off_app:
    print('''Bienvenido. Este es el menú inicial.
          Elija el número de la siguiente lista de opciones 
          
          1. Contestar encuesta.
          2. Visualizar resultados. 
          0. Apagar programa.''')
    
    option = input("Ingrese el número seleccionado ahora: ")

    match option:
        case "1": 
            print("-"*50)
            print("Iniciando encuesta:")
            nuevo_registro = encuesta()
            print("-"*50)
            add_regis(nuevo_registro)
            input("Presione ENTER para volver al menú principal")
            print("-"*50)

        case "2":
             while sub_menu_activo:
                #Reinician las variables de estadística.
                total_regis = 0
                total_lt = 0
                total_updt = 0
                total_score = 0

                print("-"*50)
                print('''Menú de visualización de datos:
                1. Buscar estadísticas por marca.
                2. Buscar estadísticas por modelo.
                3. Mostrar todos los registros.
                4. Volver al menú principal.''')

                sub_option = input("Ingrese su opción: ").strip()
                

                match sub_option:
                    case "1":
                        print("-"*50)
                        req_marca = input("Ingrese la marca a buscar: ").strip()
                        regis_scan(data_by_brand, req_marca)
                        print("-"*50)
                        input("Presione ENTER para continuar...")

                    case "2":
                        modelo_buscado = input("Ingrese el modelo que desea consultar: ").strip()

                        regis_scan(data_by_model, False, modelo_buscado)
                        input("Presione ENTER para continuar...")

                    case "3":
                        regis_scan(show_regis)
                        input("Presione ENTER para continuar...")

                    case "4":
                        print("-"*50)
                        break

                    case _:
                        print("Opción inválida. Intente nuevamente.")

        case "0":
            print("Gracias por utilizar el programa. Recuerde siempre cuidar sus dispositivos móviles.")
            on_off_app = False
        case _: print("Opción inválida. Intente nuevamente.") 