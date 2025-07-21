on_off_app = True
disp_data = {}

while on_off_app:
    print('''Bienvenido. Este es el menú inicial.
          Elija el número de la siguiete lista de opciones 
          
          1. Contestar encuesta.
          2. Visualizar resultados. 
          0. Apagar programa''')
    
    option = input("Ingrese el número seleccionado ahora:")

    match option:
        case "1": 
            print("Sección para contestar encuesta.")
            option = ("Presione ENTER para continuar.")
        case "2":
            print("Sección para visualizar resultado.")
            option = ("Presione ENTER para continuar.")
        case "0":
            print("Gracias por utilizar el programa. Recuerde siempre cuidar sus dispositivos móviles.")
            on_off_app = False
    