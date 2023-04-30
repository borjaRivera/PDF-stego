#!/usr/bin/python

import os, sys
from PIL import Image
from utils import rgb_to_binary, add_leading_zeros

class Encoder():

	def hide_image(img_visible_path, img_hidden_path, output_path):
		"""
		Opens two specified images, an image we want to conceal and an image we want to use for concealing,
		hides the image information in the binary pixel values of the other image and saves
		the resulting image in a specified location or the default location if no location is specified.

		The number of pixels in the image used for hiding an image must be at least (2 * number of pixels in the image to be
		hidden + 1)
		"""

		img_visible = Image.open(img_visible_path)
		img_hidden = Image.open(img_hidden_path)

		encoded_image = Encoder.encode(img_visible, img_hidden)

		encoded_image.save(output_path)

	def get_binary_pixel_values(img, width, height):
		"""
		Retrieves a string of concatenated binary representations of RGB channel values of all pixels in an image.

		Returns:
			A string with concatenated binary numbers representing the RGB channel values of all pixels in the image
			where each binary number representing one channel value is 8 bits long, padded with leading zeros 
			when necessary. Therefore, each pixel in the image is represented by 24 bit long binary sequence.
		"""
		hidden_image_pixels = ''
		for col in range(width):
			for row in range(height):
				pixel = img[col, row]
				r=0
				g=0
				b=0
				if(pixel==0):
					r=0
					g=0
					b=0
				elif (pixel==255):
					r = 255
					g = 255
					b = 255
				else:
					r=pixel[0]
					g=pixel[1]
					b=pixel[2]
				r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
				hidden_image_pixels += r_binary + g_binary + b_binary
		return hidden_image_pixels

	def change_binary_values(img_visible, hidden_image_pixels, width_visible, height_visible, width_hidden, height_hidden):
		"""
		Replaces the 4 least significant bits of a subset of pixels in an image with bits representing a sequence of binary
		values of RGB channels of all pixels of the image to be concealed.

		The first pixel in the top left corner is used to store the width and height of the image to be hidden, which is
		necessary for recovery of the hidden image.

		Returns:
			An RGB image which is a copy of img_visible where the 4 least significant bits of a subset of pixels
			are replaced with bits representing the hidden image.
		"""
		idx = 0
		for col in range(width_visible):
			for row in range(height_visible):
				if row == 0 and col == 0:
					width_hidden_binary = add_leading_zeros(bin(width_hidden)[2:], 12)
					height_hidden_binary = add_leading_zeros(bin(height_hidden)[2:], 12)
					w_h_binary = width_hidden_binary + height_hidden_binary
					img_visible[col, row] = (int(w_h_binary[0:8], 2), int(w_h_binary[8:16], 2), int(w_h_binary[16:24], 2))
					continue
				r, g, b = img_visible[col, row]
				r_binary, g_binary, b_binary = rgb_to_binary(r, g, b)
				r_binary = r_binary[0:4] + hidden_image_pixels[idx:idx+4]
				g_binary = g_binary[0:4] + hidden_image_pixels[idx+4:idx+8]
				b_binary = b_binary[0:4] + hidden_image_pixels[idx+8:idx+12]
				idx += 12
				img_visible[col, row] = (int(r_binary, 2), int(g_binary, 2), int(b_binary, 2))
				if idx >= len(hidden_image_pixels):
					return img_visible
		# can never be reached, but let's return the image anyway
		return img_visible

	def encode(img_visible, img_hidden):
		"""
		Loads the image to be hidden and the image used for hiding and conceals the pixel information from one image
		in the other one.

		Returns:
			An RGB image which is supposed to be not very different visually from img_visible, but contains all the information
			necessary to recover an identical copy of the image we want to hide.
		"""
		encoded_image = img_visible.load()
		#print(encoded_image[0, 0])
		img_hidden_copy = img_hidden.load()
		#print(img_hidden_copy[0, 0])
		width_visible, height_visible = img_visible.size
		width_hidden, height_hidden = img_hidden.size
		hidden_image_pixels = Encoder.get_binary_pixel_values(img_hidden_copy, width_hidden, height_hidden)
		encoded_image = Encoder.change_binary_values(encoded_image, hidden_image_pixels, width_visible, height_visible, width_hidden, height_hidden)
		return img_visible

	

#if __name__ == '__main__':
#	Encoder.hide_image("qr_coldplay_bueno.png", "qr_random_key_ciphered.png", "qr_test_definitivo.png")


