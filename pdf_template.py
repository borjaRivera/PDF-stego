from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image


class PdfTemplate:

    def create(pdf_name, image_name, qr_name):
        # Información del concierto
        nombre_artista = "Coldplay"
        fecha = "28 de mayo de 2023"
        hora = "21:30h"
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
        tabla = Table([
            [Paragraph("<b>Fecha:</b>", estilo_normal), fecha],
            [Paragraph("<b>Hora:</b>", estilo_normal), hora],
            [Paragraph("<b>Lugar:</b>", estilo_normal), lugar],
            [Paragraph("<b>Precio:</b>", estilo_normal), precio],
            [Paragraph("<b>Nombre del comprador:</b>", estilo_normal), nombre_comprador],
            [Paragraph("<b>Asiento:</b>", estilo_normal), asiento],
            [Paragraph("<b>Código QR:</b>", estilo_normal), Image(qr_name, 100, 100)]
        ], colWidths=[2.5 * inch, 4.5* inch])
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#FAD000")),
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
        texto_legal = "Esta entrada es válida solo para el portador nombrado en la misma y no puede ser transferida, revendida o duplicada. En caso de pérdida o robo no se emitirán duplicados. La entrada no garantiza la disponibilidad de un asiento específico y puede ser reubicada en caso de necesidad."
        contenido.append(Paragraph(texto_legal, estilo_normal))

        # Añadir el contenido al PDF y cerrarlo
        doc.build(contenido)