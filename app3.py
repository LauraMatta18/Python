"""
    En este proyecto espero que hagas lo siguiente:
    - Crear un programa que:
        - solicitar al usuario el nombre del archivo de texto que se creará
        - Preguntar al usuario el nombre de la frase que debe escribirse en este archivo
        - Ensambla el código que toma el nombre del archivo y la frase escrita y crea este archivo
        - crear otro archivo (en el mismo archivo) que ingresa a este archivo que acaba de crear, lee su contenido y lo imprime en la pantalla
        - Confirme que todo funciona, hacer que este archivo sea ejecutable, como se enseño en la clase anterior
"""
#solicitar al usuario el nombre del archivo de texto que se creará

nombre_archivo = input("Ingresa el nombre del archivo de texto que se creará, pero no uses extensión : ")+  ".txt"

#Preguntar al usuario el nombre de la frase que debe escribirse en este archivo

frase = input("Escriba la frase que desea guardar en el archivo : ")

#Crear el archivo y escribir la frase
with open(nombre_archivo, "w") as archivo:
    archivo.write(frase)
print(f"\nLa frase se ha guardado en el archivo '{nombre_archivo}' con éxito")

#Leer el archivo y imprimir su contenido
with open(nombre_archivo, "r") as archivo:
    contenido = archivo.read()
print("\nContenido del archivo leído:")
print(contenido)
