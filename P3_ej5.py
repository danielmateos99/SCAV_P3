import os

exit = True
while exit == True:

    print("Selecciona un ejercicio: ")
    print("[1]: Crear el archivo container.mp4")
    print("[2]: Crea tu propio container mp4 con un vídeo, audio y subtítulos")
    print('[3]: Leer "tracks" de un container mp4')
    print('[4]: "Testing sript" para el ejercicio 3')
    print("[5]: Exit")

    a = input()
    x = int (a)
    print(" ")

    if x == 1:
        #Llamar al script de python que realiza el ejercicio 1
        os.system('python P3_ej1.py')
    elif x == 2:
        #Llamar al script de python que realiza el ejercicio 2
        os.system('python P3_ej2.py')
    elif x == 3:
        #Llamar al script de python que realiza el ejercicio 3
        os.system('python P3_ej3.py')
    elif x == 4:
        #Llamar al script de python que realiza el ejercicio 4
        os.system('python P3_ej4.py')
    elif x == 5:
        #Salir del menú
        exit = False
    else:
        #En caso de que no se elija ninguna de las opciones
        print('Error: Introduce alguno de los valores mencionados.')
