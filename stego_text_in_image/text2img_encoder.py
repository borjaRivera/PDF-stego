from PIL import Image
import math 

class TextEncoder():

	final_char = [1, 1, 1, 1, 1, 1, 1, 1]


	def get_ascii(character):
		return ord(character)

	def get_binary(number):
		return bin(number)[2:].zfill(8)

	def change_last_bit(byte, new_bit):
		return byte[:-1] + str(new_bit)

	def binary_to_decimal(binary):
		return int(binary, 2)

	def modify_color(color_original, bit):
		color_in_binary = TextEncoder.get_binary(color_original)
		color_modified = TextEncoder.change_last_bit(color_in_binary, bit)

		return TextEncoder.binary_to_decimal(color_modified)

	def get_bits(text):
		lista = []
		for character in text:
			character_ascii = TextEncoder.get_ascii(character)
			character_binary = TextEncoder.get_binary(character_ascii)
			for bit in character_binary:
				lista.append(bit)
		for bit in TextEncoder.final_char:
			lista.append(bit)
		return lista

	def hide(msg, origin_img_path, destination_img_path="output.png"):
		#print("Hidding message...".format(msg))
		img = Image.open(origin_img_path)
		pixels = img.load()

		img_size = img.size
		img_width = img_size[0]
		img_height = img_size[1]

		pixels_list = TextEncoder.get_bits(msg)
		counter = 0
		pixels_list_length = len(pixels_list)

		for x in range(img_width):
			for y in range(img_height):
				if counter < pixels_list_length:
					pixel = pixels[x, y]

					red = pixel[0]
					green = pixel[1]
					blue = pixel[2]

					if counter < pixels_list_length:
						red_modified = TextEncoder.modify_color(red, pixels_list[counter])
						counter += 1
					else:
						red_modified = red

					if counter < pixels_list_length:
						green_modified = TextEncoder.modify_color(green, pixels_list[counter])
						counter += 1
					else:
						green_modified = green

					if counter < pixels_list_length:
						blue_modified = TextEncoder.modify_color(blue, pixels_list[counter])
						counter += 1
					else:
						blue_modified = blue

					pixels[x, y] = (red_modified, green_modified, blue_modified)
				else:
					break
			else:
				continue
			break

		if counter >= pixels_list_length:
			print("\n[OK] Message hidden correctly")
			img.save(destination_img_path)
			result = True
		else:
			print("\nDanger: not able to write the message, left {} characters".format( math.floor((pixels_list_length - counter) / 8) ))
			result = False

		return result

