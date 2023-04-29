from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image




class PdfTemplate:

    
    def create(pdf_name, image_name, qr_name, secret_code):
        number = "6"



        # Información del concierto
        nombre_artista = "Coldplay"
        fecha = "28 de mayo de 2023"
        hora = "21:30h      "
        lugar = "Estadio Santiago Bernabéu"
        precio = "150 €"
        nombre_comprador = "Florentino Pérez"
        asiento = "Sección A, Fila 10, Asiento 5"
        gira = "Coldplay - Music Of The Spheres World Tour 21:30h"


        # Estilos para los elementos del PDF
        estilo_normal = getSampleStyleSheet()["Normal"]
        estilo_titulo = getSampleStyleSheet()["Heading1"]
        estilo_titulo.alignment = 0 
        estilo_subtitulo = getSampleStyleSheet()["Heading2"]
        estilo_subtitulo.alignment = 0

        # Crear el PDF
        doc = SimpleDocTemplate(pdf_name, pagesize=letter)
        contenido = []

        # Título del PDF
        contenido.append(Paragraph("Esta es tu entrada 1 de 1", estilo_titulo))
        #contenido.append(Spacer(1, 0.2 * inch))
        contenido.append(Paragraph(gira, estilo_subtitulo))
        contenido.append(Spacer(1, 0.1 * inch))

        # Imagen
        imagen = Image(image_name, width=7*inch, height=3.5*inch)
        contenido.append(imagen)
        contenido.append(Spacer(1, 0.2 * inch))

        # Tabla con la información del concierto y el código QR
        fecha_header = "Fecha:"
        fecha_espacios = " " * int(secret_code[0])  # espacios * secret_code[0]
        fecha_final_header = "{}{}".format(fecha_header, fecha_espacios)

        hora_header = "Hora:"
        hora_espacios = " " * int(secret_code[1])  # espacios * secret_code[0]
        hora_final_header = "{}{}".format(hora_header, hora_espacios)

        lugar_header = "Lugar:"
        lugar_espacios = " " * int(secret_code[2])  # espacios * secret_code[0]
        lugar_final_header = "{}{}".format(lugar_header, lugar_espacios)

        precio_header = "Precio:"
        precio_espacios = " " * int(secret_code[3])# espacios * secret_code[0]
        precio_final_header = "{}{}".format(precio_header, precio_espacios)

        tabla = Table([
            [fecha_final_header, fecha],
            [hora_final_header, hora],
            [lugar_final_header, lugar],
            [precio_final_header, precio],
            [Paragraph("<b>Nombre del comprador:</b>", estilo_normal), nombre_comprador],
            [Paragraph("<b>Asiento:</b>", estilo_normal), asiento],
            [Paragraph("<b>Código QR:</b>", estilo_normal), Image(qr_name, 100, 100)]
        ], colWidths=[2.5 * inch, 4.5* inch])
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#333333")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#FFFFFF")),
            ("ALIGNMENT", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 12),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
            ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold")
        ]))


        # Añadir la tabla al contenido del PDF
        contenido.append(tabla)


        # Nota legal
        texto_legal = """Organiza: B66255233 CYCLOP 2014 S.L.. La adquisición de esta entrada representa la aceptación de las siguientes condiciones: La organización no garantiza la autenticidad y no se responsabiliza de las
        entradas adquiridas fuera de los puntos de venta oficiales. Este canal no se hace responsable de cualquier diferencia de precio respecto a entradas adquiridas a través de otros canales de venta. No se
        admiten cambios ni devoluciones, salvo por causas previstas en la legislación vigente. La organización se reserva todos los derechos de imagen y propiedad intelectual del espectáculo, quedando prohibida
        cualquier filmación, grabación o reproducción en el interior del recinto sin la autorización expresa del organizador. El público podrá ser objeto de registro a la entrada del recinto de acuerdo con la Ley.
        Queda prohibida la introducción de toda clase de armas y objetos arrojadizos o peligrosos. Se reserva el derecho de admisión por razones de orden público. No se permitirá la entrada al recinto a las
        personas que se encuentren bajo los efectos de bebidas alcohólicas, estupefacientes, psicotrópicos, estimulantes o sustancias análogas o sean portadores de ellas. La entrada deberá conservase completa
        y en buen estado, pudiendo denegarse la admisión en caso contrario. Toda entrada enmendada, rota, en mal estado o con condiciones de falsificación, autorizará al organizador a denegar la entrada al
        recinto. El organizador podrá negar o expulsar del recinto al portador en caso de incumplimiento de las indicaciones del personal de la organización. El canal únicamente gestiona la distribución de entradas
        por cuenta del organizador, por lo que queda expresamente eximido de toda obligación y/o responsabilidad que compete al organizador. Toda reclamación sobre la realización, suspensión, modificación o
        anulación del espectáculo deberá dirigirse al organizador cuyos datos constan en esta misma entrada. Las relaciones jurídicas, derecho y obligaciones derivadas de la tenencia de esta entrada estarán
        sujetas en todo momento a lo establecido por las leyes españolas vigentes."""
        contenido.append(Paragraph(texto_legal, estilo_normal))

        # Añadir el contenido al PDF y cerrarlo
        doc.build(contenido)


if __name__ == '__main__':

	PdfTemplate.create("prueba.pdf", "./images/coldplay_image.png", "./images/coldplay_qr.png", "9999")
        
    