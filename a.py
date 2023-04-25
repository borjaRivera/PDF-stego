    def create(pdf_name, image_name, qr_name):

        # data which we are going to be displayed in a  tabular format

        tableData = [

        ["Date", "Course Name", "Course Type", "Course Price (Rs.)"],

        ["4/6/2021","Video Editing using Filmora X","Online Self-paced","1,500.00/-",],

        ["16/2/2021","Advanced Ethical Hacking","Online Live","8,000.00/-"],

        ["12/1/2021", "Data Science using Python","Offline Course","9,800.00/-"],

        ["02/5/2021","Technical Writing","Online Free","2,439.00/-"],

        ["Signature", "", "", "_________________"],

        ]



        # creating a Document structure with A4 size page

        docu = SimpleDocTemplate(pdf_name, pagesize=A4)

        styles = getSampleStyleSheet()



        doc_style = styles["Heading1"]

        doc_style.alignment = 1



        title = Paragraph("COURSE INVOICE", doc_style)

        style = TableStyle([

                ("BOX", (0, 0), (-1, -1), 1, colors.black),

                ("GRID", (0, 0), (4, 4), 1, colors.chocolate),

                ("BACKGROUND", (0, 0), (3, 0), colors.skyblue),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ])

        # creates a table object using the Table() to pass the table data and the style object

        table = Table(tableData, style=style)

        
        qr = Image(qr_name, 75, 75)

        main_image = Image(image_name, 250, 150)

        # finally, we have to build the actual pdf merging all objects together

        docu.build([title, table, main_image, qr])