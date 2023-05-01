import json
import os

import requests
from bs4 import BeautifulSoup


COMPANIES_JSON_PATH = "src/companies.json"
companiesJson = json.load(open(COMPANIES_JSON_PATH))

companies = companiesJson["companies"]
for company in companies:
	ycdbHtmlPath = f"cache/{company['codeName']}.ycdb.html"
	soup = BeautifulSoup(open(ycdbHtmlPath), "lxml")

	imgs = soup.find_all("img")
	imgSrcs = [x['src'] for x in imgs]
	externalImgSrcs = [x for x in imgSrcs if x.startswith("https://")]

	logoPath = f"logos/{company['codeName']}.logo.png"
	if os.path.isfile(logoPath):
		print(f"Found: {logoPath}")
		continue

	logoURL = externalImgSrcs[0]
	screenshotURL = None if len(externalImgSrcs) == 1 else externalImgSrcs[1]

	print(f"Downloading {logoURL} ...")
	res = requests.get(logoURL)
	if res.status_code == 200:
		with open(logoPath, "wb") as f:
			f.write(res.content)
		print(f"\tSaved: {logoPath}")

	# break


