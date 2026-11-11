import string

lista_palabras = ["libre", "quiero", "ser", "vida", "amigos", "saber"]

def contar_palabras(lista_palabras, archivo):

    with open(archivo, "r", encoding="utf-8") as txt:
        contenido = txt.read()

    contenido = contenido.lower()

    for signo in string.punctuation:
        contenido = contenido.replace(signo, " ")

    palabras_texto = contenido.split()

    diccionario = {}

    for palabra in lista_palabras:
        diccionario[palabra] = palabras_texto.count(palabra)

    return diccionario


resultado = contar_palabras(lista_palabras, "problema2.txt")

print("Resultado de la búsqueda:")
for palabra in sorted(resultado):
    print(palabra, ":", resultado[palabra])


# NOTAS:

# open(): abre un archivo para poder leerlo o escribir en él.
# read(): lee todo el contenido de un archivo y lo devuelve como una cadena de texto (str).
# lower(): convierte todas las letras de un texto a minúsculas.
# replace(): sustituye una parte de un texto por otra.
# split(): divide un texto en palabras y devuelve una lista.
# count(): cuenta cuántas veces aparece un elemento.
# sorted(): devuelve una lista con los elementos ordenados.
