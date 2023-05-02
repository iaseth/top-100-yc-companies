import json
import math
import os

import requests
from bs4 import BeautifulSoup
from colorthief import ColorThief
from PIL import Image
import numpy


COMPANIES_JSON_PATH = "companies.json"
PALETTES_JSON_PATH = "src/palettes.json"

def clamp(x):
	return max(0, min(x, 255))

def rgb_to_hex(rgb):
	return "#{0:02x}{1:02x}{2:02x}".format(clamp(rgb[0]), clamp(rgb[1]), clamp(rgb[2]))


def file_save_log(filepath):
	size = os.path.getsize(filepath)
	kB = round(size / 1000, 1)
	print(f"Saved: {filepath} [{kB}kB]")


def downloadLogo(soup, logoPath):
	if os.path.isfile(logoPath):
		print(f"\tFound: {logoPath}")
		return

	imgs = soup.find_all("img")
	imgSrcs = [x['src'] for x in imgs]
	externalImgSrcs = [x for x in imgSrcs if x.startswith("https://")]

	logoURL = externalImgSrcs[0]
	screenshotURL = None if len(externalImgSrcs) == 1 else externalImgSrcs[1]

	print(f"\tDownloading {logoURL} ...")
	res = requests.get(logoURL)
	if res.status_code == 200:
		with open(logoPath, "wb") as f:
			f.write(res.content)
		print(f"\t\tSaved: {logoPath}")


def downloadMeta(soup, logoPath, company):
	metaJsonPath = f"meta/{company['metaJsonName']}"
	if os.path.isfile(metaJsonPath):
		print(f"\tFound: {metaJsonPath}")
		# return

	ct = ColorThief(logoPath)
	palette = ct.get_palette(color_count=5)
	palette_png_path = f"palettes/{company['codeName']}.palette.png"

	jo = dict(company)
	a = soup.find("a", class_="btn btn-primary btn-block mt-4")
	jo["website"] = a["href"]
	jo["palette"] = palette
	jo["hexPalette"] = [rgb_to_hex(rgb) for rgb in palette]
	jo["metaJsonPath"] = metaJsonPath
	jo["logoPngPath"] = logoPath
	jo["palettePngPath"] = palette_png_path

	with open(metaJsonPath, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"\tSaved: {metaJsonPath}")

	if os.path.isfile(palette_png_path):
		print(f"\tFound: {palette_png_path}")
	else:
		SIZE = 200
		SIZE_Y = SIZE * len(palette)
		data = numpy.zeros((SIZE, SIZE_Y, 3), dtype=numpy.uint8)
		for x in range(SIZE):
			for y in range(SIZE_Y):
				cid = math.floor(y / SIZE)
				data[x][y] = palette[cid]

		im = Image.fromarray(data)
		im.save(palette_png_path)
		file_save_log(palette_png_path)

	return jo


def main():
	companiesJson = json.load(open(COMPANIES_JSON_PATH))
	companies = companiesJson["companies"]
	palettes = []
	for idx, company in enumerate(companies):
		print(f"[{idx+1}/{len(companies)}] {company['name']}")
		ycdbHtmlPath = f"cache/{company['codeName']}.ycdb.html"
		soup = BeautifulSoup(open(ycdbHtmlPath), "lxml")

		logoPath = f"logos/{company['logoPngName']}"
		downloadLogo(soup, logoPath)
		palette = downloadMeta(soup, logoPath, company)
		palettes.append(palette)
		# break

	jo = {}
	jo["palettes"] = palettes
	with open(PALETTES_JSON_PATH, "w") as f:
		json.dump(jo, f, indent="\t")
	file_save_log(PALETTES_JSON_PATH)


if __name__ == '__main__':
	main()
