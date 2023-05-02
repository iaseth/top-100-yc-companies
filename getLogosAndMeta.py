import json
import os

import requests
from bs4 import BeautifulSoup


COMPANIES_JSON_PATH = "src/companies.json"

def downloadLogo(soup, company):
	logoPath = f"logos/{company['logoPngName']}"
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


def downloadMeta(soup, company):
	metaPath = f"meta/{company['metaJsonName']}"
	if os.path.isfile(metaPath):
		print(f"\tFound: {metaPath}")
		# return

	jo = {}
	a = soup.find("a", class_="btn btn-primary btn-block mt-4")
	jo["website"] = a["href"]

	with open(metaPath, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"\tSaved: {metaPath}")


def main():
	companiesJson = json.load(open(COMPANIES_JSON_PATH))
	companies = companiesJson["companies"]
	for idx, company in enumerate(companies):
		print(f"[{idx+1}/{len(companies)}] {company['name']}")
		ycdbHtmlPath = f"cache/{company['codeName']}.ycdb.html"
		soup = BeautifulSoup(open(ycdbHtmlPath), "lxml")
		downloadLogo(soup, company)
		downloadMeta(soup, company)
		# break


if __name__ == '__main__':
	main()
