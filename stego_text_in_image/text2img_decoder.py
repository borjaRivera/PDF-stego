from PIL import Image

class TextDecoder():

	final_char = "11111111"

	def get_lsb(byte):
		return byte[-1]

	def get_binary(number):
		return bin(number)[2:].zfill(8)

	def binary_to_decimal(binary):
		return int(binary, 2)

	def get_ascii(number):
		return chr(number)

	def read(ruta_imagen):
		img = Image.open(ruta_imagen)
		pixels = img.load()

		img_size = img.size
		img_width = img_size[0]
		img_heigth = img_size[1]

		byte = ""
		msg = ""

		for x in range(img_width):
			for y in range(img_heigth):
				pixel = pixels[x, y]

				red = pixel[0]
				green = pixel[1]
				blue = pixel[2]


				byte += TextDecoder.get_lsb(TextDecoder.get_binary(red))
				if len(byte) >= 8:
					if byte == TextDecoder.final_char:
						break
					msg += TextDecoder.get_ascii(TextDecoder.binary_to_decimal(byte))
					byte = ""

				byte += TextDecoder.get_lsb(TextDecoder.get_binary(green))
				if len(byte) >= 8:
					if byte == TextDecoder.final_char:
						break
					msg += TextDecoder.get_ascii(TextDecoder.binary_to_decimal(byte))
					byte = ""

				byte += TextDecoder.get_lsb(TextDecoder.get_binary(blue))
				if len(byte) >= 8:
					if byte == TextDecoder.final_char:
						break
					msg += TextDecoder.get_ascii(TextDecoder.binary_to_decimal(byte))
					byte = ""

			else:
				continue
			break
		return msg