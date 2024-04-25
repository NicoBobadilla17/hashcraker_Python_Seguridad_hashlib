#decifrador de funciones hash con diccionario
#comparando valores con una lista de palabras en el diccionario
#verificar si algunas de las palabras esta dentro del diccionario
#si alguna de las palabras logra al mismo hash quiere decir que lo desiframos
#hash a decifrar "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
import hashlib

hash_file = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08" #hash a decifar en variable

dic_file = input("ingrese la direccion del archivo del diccionario: ")#input del usuario para que ingrese el archivo del diccionario

with open(dic_file,'r') as file: #variable donde se guarda el directorio, el parametro "r" de read para leer el archivo

    diccionario = [line.strip() for line in file] #recorrera cada linea del archivo del diccionario "line.strip"nos permite eliminar espacios antes y despues de las palabras del diccionario
    
    for password in diccionario: #recorrera cada password del diccionario y calcular el hash
        
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()
        #calcula cada hash con la libreberia hashlib.sha256 por que el formato del hash es sha256
        
        if hash_calculado == hash_file:
            print("la contraseña es: " + password)
            break
        else:
            print("no se encontro la contraseña en el diccionario: ")