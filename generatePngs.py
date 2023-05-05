import json
import math
import os

from PIL import Image
import numpy



def hexToRgb(hex):
	hex = hex.lstrip('#')
	rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
	return rgb


def paletteToPngStrip(colors, pngPath):
	if os.path.isfile(pngPath):
		print(f"\tFound: {pngPath}")
		return

	SIZE = 200
	SIZE_Y = SIZE * len(colors)
	data = numpy.zeros((SIZE, SIZE_Y, 3), dtype=numpy.uint8)
	for x in range(SIZE):
		for y in range(SIZE_Y):
			cid = math.floor(y / SIZE)
			data[x][y] = colors[cid]

	im = Image.fromarray(data)
	im.save(pngPath)
	print(f"\tSaved: {pngPath}")


def paletteToPngStack(colors, pngPath):
	if os.path.isfile(pngPath):
		print(f"\tFound: {pngPath}")
		return

	SIZE = 100
	SIZE_X = SIZE * len(colors)
	SIZE_Y = 500

	data = numpy.zeros((SIZE_X, SIZE_Y, 3), dtype=numpy.uint8)
	for x in range(SIZE_X):
		cid = math.floor(x / SIZE)
		for y in range(SIZE_Y):
			data[x][y] = colors[cid]

	im = Image.fromarray(data)
	im.save(pngPath)
	print(f"\tSaved: {pngPath}")


def main():
	tailwindcolorsJson = json.load(open("src/tailwindcolors.json"))
	colorNames = tailwindcolorsJson.keys()
	for idx, colorName in enumerate(colorNames):
		palette = tailwindcolorsJson[colorName]
		hexColors = [hex for hex in palette.values()]
		colors = [hexToRgb(hex) for hex in hexColors]
		print(f"{idx+1}. Color: {colorName}")

		pngStripPath = f"png/standard/{colorName}.strip.png"
		paletteToPngStrip(colors, pngStripPath)

		pngStackPath = f"png/standard/{colorName}.stack.png"
		paletteToPngStack(colors, pngStackPath)
		# break


if __name__ == '__main__':
	main()
