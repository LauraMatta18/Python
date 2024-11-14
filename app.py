"""
"w" - usado para escribir en archivos, apagando el contenido existent
"r" - usado para leer archivos
"a" - usado para agregar texto al final de un archivo
"r+" - usado para leer y escribir en archivos
"""

#Crear un archivo (apagando el contenido)
# Abrimos el archivo
#with open("archivo.txt", "w") as archivo:
    # Escribimos en el archivo
    #archivo.write("archivo : 12345")
    
#Agregar texto al final del archivo (no apagando el contenido)
#with open("archivo.txt", "a") as archivo:
    # Escribimos en el archivo
    #archivo.write("archivo : 6789")
    
#Leer archivo
#with open("archivo.txt", "r") as archivo:
    #for linea in archivo:
        #print(linea)
        
#Leer y escribir en archivo al tiempo
with open("archivo.txt", "r+") as archivo:
    for linea in archivo:
        print(linea)
    archivo.write("Nueva linea")