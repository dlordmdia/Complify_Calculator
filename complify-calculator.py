# Imports
import time
import webbrowser

# Variables
decidido = False
seguir = "y"

# Start
print("\n----COMPLIFY CALCULATOR----\n    Made by @dlordmdia\n\n")

# About
print("QUE ES?\n Esto es una calculadora con un montón de funciones y actividades divertidas incluidas en ella!\n\nPARA QUE SIRVE?\n Con esta calculadora puedes concentrarte y personalizar tu tiempo de estudio o cálculo!\n\n")
input("Presiona ///ENTER\\\ para Seguir\n- ")

# Personalización
while not decidido:
    start = input("Que quieres personalizar?\nType -h for help\n- ")
    if start == "h":
        print("NECESITAS AYUDA?\nPresiona -m si quieres escuchar música\nPresiona -l para ser Redirigido a Classroom\nPresiona -d para ser Redirigido a Google Drive\nPresiona -g para ser Redirigido a Google\nPresiona -c si quieres ver el código\nPresiona -s para Saltar la Personalización o Seguir el Cálculo\nPresiona -e para cerrar la calculadora\n\n")
    if start == "m":
        dec1 = input("Que quieres escuchar?\na) Música chill\nb) Playlist Random\n- ")
        if dec1 == "a":
            webbrowser.open("https://www.youtube.com/watch?v=cD0szT7pOcc")
        elif dec1 == "b":
            webbrowser.open("https://www.youtube.com/watch?v=R2AJOOvZgbc&list=PLNawVVX6lTrQmEqCXKAFlYEHf-fveJc22")
        else:
            print("Te habrás equivocado de tecla... Intentalo de nuevo!")
    elif start == "c":
        print("Redirigiendo a GitHub...")
        webbrowser.open("https://github.com/dlordmdia")
    elif start == "s":
        print("Saltando Personalización...")
        time.sleep(0.5)
        print("Redirigiendo al cálculo...\n")
        time.sleep(0.5)
        break
    elif start == "e":
        print("Gracias por usar Complify Calculator\n--Creado por @dlordmdia--\n")
        exit()
    elif start == "l":
        print("Redirigiendo a Classroom...\n")
        time.sleep(1)
        webbrowser.open("https://www.classroom.google.com")
    elif start == "d":
        print("Redirigiendo a Google Drive...\n")
        time.sleep(1)
        webbrowser.open("https://www.drive.google.com")
    elif start == "g":
        print("Redirigiendo a Google...\n")
        time.sleep(1)
        webbrowser.open("https://www.google.com")

# Cálculo
while seguir == "y":
    equation = input("\nCuál es tu ecuación?\n")
    print(f"Resultado: {eval(equation)}\n")
    time.sleep(2)
    seguir = input("Quieres hacer otro calculo? (y/n): ")
time.sleep(0.5)
print("\nGracias por usar Complify Calculator\n--Creado por DlordMDia--\n")
time.sleep(1)
print("Enviándote a GitHub...")
time.sleep(1)
webbrowser.open("https://github.com/dlordmdia")