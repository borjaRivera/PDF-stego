from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph, Image




class PdfTemplate:

    """
    Here we create the template for the PDF to be generated    
    """
    def create(pdf_name, image_name, qr_name, secret_code):

        # Concert Information
        date = "28 de mayo de 2023"
        time = "21:30h"
        place = "Estadio Santiago Bernabéu"
        cost = "150 €"
        buyer_name = "Florentino Pérez"
        chair_number = "Sección A, Fila 10, Asiento 5"
        tour = "Coldplay - Music Of The Spheres World Tour 21:30h"


        # Styles for the PDF elements
        normal_style = getSampleStyleSheet()["Normal"]
        title_style = getSampleStyleSheet()["Heading1"]
        title_style.alignment = 0 
        subtitle_style = getSampleStyleSheet()["Heading2"]
        subtitle_style.alignment = 0

        # Create PDF
        doc = SimpleDocTemplate(pdf_name, pagesize=letter)
        content = []

        # PDF Title
        content.append(Paragraph("Esta es tu entrada 1 de 1", title_style))
        #contenido.append(Spacer(1, 0.2 * inch))
        content.append(Paragraph(tour, subtitle_style))
        content.append(Spacer(1, 0.1 * inch))

        # Image
        image = Image(image_name, width=7*inch, height=3.5*inch)
        content.append(image)
        content.append(Spacer(1, 0.2 * inch))

        # Information chart and QR Code
        header_date = "Fecha:"
        date_spaces = " " * int(secret_code[0])  # espacios * secret_code[0]
        date_final_header = "{}{}".format(header_date, date_spaces)

        time_header = "Hora:"
        time_espacios = " " * int(secret_code[1])  # espacios * secret_code[1]
        time_final_header = "{}{}".format(time_header, time_espacios)

        place_header = "Lugar:"
        place_espacios = " " * int(secret_code[2])  # espacios * secret_code[2]
        place_final_header = "{}{}".format(place_header, place_espacios)

        cost_header = "Precio:"
        cost_espacios = " " * int(secret_code[3])# espacios * secret_code[3]
        cost_final_header = "{}{}".format(cost_header, cost_espacios)

        chart = Table([
            [date_final_header, date],
            [time_final_header, time],
            [place_final_header, place],
            [cost_final_header, cost],
            [Paragraph("<b>Nombre del comprador:</b>", normal_style), buyer_name],
            [Paragraph("<b>Asiento:</b>", normal_style), chair_number],
            [Paragraph("<b>Código QR:</b>", normal_style), Image(qr_name, 100, 100)]
        ], colWidths=[2.5 * inch, 4.5* inch])
        chart.setStyle(TableStyle([
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
        content.append(chart)


        # Nota legal
        legal_content = """Organiza: B66255233 CYCLOP 2014 S.L.. La adquisición de esta entrada representa la aceptación de las siguientes condiciones: La organización no garantiza la autenticidad y no se responsabiliza de las
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
        content.append(Paragraph(legal_content, normal_style))

        # Añadir el contenido al PDF y cerrarlo
        doc.build(content)


#if __name__ == '__main__':
#	PdfTemplate.create("prueba.pdf", "./images/coldplay_image.png", "./images/coldplay_qr.png", "9999")
        
    