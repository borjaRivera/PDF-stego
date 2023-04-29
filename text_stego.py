import fitz
from hiding import show
doc = fitz.open('a.pdf')
text = ""
for page in doc:
   text+=page.get_text()


text_array = text.split("\n")
fecha = text_array[2]
hora = text_array[4]
lugar = text_array[6]
precio = text_array[8]


print(text_array)

print("Espacios en Fecha: " + str(fecha.count(" ")))
print("Espacios en Hora: " + str(hora.count(" ")))
print("Espacios en Lugar: " + str(lugar.count(" ")))
print("Espacios en Precio: " + str(precio.count(" ")))

