#Import required dependencies
import fitz
import os
from PIL import Image
import cv2

class Extractor():

    """
    This method checks if the image that is sent as argument contains a QR Code or not
    """
    def check_qr(qr_path):
        print("QR: ",qr_path)
        img = cv2.imread(qr_path)
        det = cv2.QRCodeDetector()
        qr_content, pts, st_code = det.detectAndDecode(img)
        print("QR Content: ", qr_content)
        print("ST_CODE: ",st_code)
        if st_code == None or st_code=="":
            print("No es QR")
            return False
        else:
            return True

    """
    This method extract all the images that appear in the file that is provided as argument
    """
    def extractImages(file_path):

        #Define path for saved images
        tmp_path = 'tmp'
        isExist = os.path.exists(tmp_path)
        if not isExist:
            os.mkdir(tmp_path)

        #Open PDF file
        pdf_file = fitz.open(file_path)

        #Get the number of pages in PDF file
        page_nums = len(pdf_file)

        #Create empty list to store images information
        images_list = []

        #Extract all images information from each page
        for page_num in range(page_nums):
            page_content = pdf_file[page_num]
            images_list.extend(page_content.get_images())

        #Raise error if PDF has no images
        if len(images_list)==0:
            raise ValueError(f'No images found in {file_path}')

        #Save all the extracted images
        for i, img in enumerate(images_list, start=1):
            #Extract the image object number
            xref = img[0]
            #Extract image
            base_image = pdf_file.extract_image(xref)
            #Store image bytes
            image_bytes = base_image['image']
            #Store image extension
            image_ext = base_image['ext']
            #Generate image file name
            image_name = str(i) + '.' + image_ext
            #Save image
            with open(os.path.join(tmp_path, image_name) , 'wb') as image_file:
                image_file.write(image_bytes)
                image_file.close()





#if __name__ == '__main__':
#	Extractor.extractImages("entrada_coldplay.pdf")