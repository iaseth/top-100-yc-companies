import json
import os

import requests
from bs4 import BeautifulSoup



TOP_100_LINK = "https://www.ycdb.co/top-companies/alexa-rank";
OUTPUT_JSON_PATH = "src/companies.json";


def getCompany(tr):
	tds = tr.find_all("td")
	data = [td.text.strip() for td in tds]

	company = {}
	company["rank"] = int(data[0])
	company["name"] = data[1]

	name = data[1].lower()
	name_chars = list(name)
	good_chars = [ch for ch in name_chars if ch.isalnum()]
	company["codeName"] = "".join(good_chars)
	company["jsonName"] = company["codeName"] + ".json"
	company["pngName"] = company["codeName"] + ".png"
	company["metaJsonName"] = company["codeName"] + ".meta.json"

	company["batch"] = data[2]
	company["category"] = data[3]
	company["description"] = data[4]
	company["alexaRank"] = int("".join(data[5].split(",")))

	relativeURL = tds[1].find('a')['href']
	company["pageURL"] = f"https://www.ycdb.co/{relativeURL[3:]}"

	return company


def main():
	res = requests.get(TOP_100_LINK)
	soup = BeautifulSoup(res.text, "lxml")

	table = soup.find("table", id="table")
	trs = table.find("tbody").find_all("tr")
	companies = [getCompany(tr) for tr in trs]

	jo = {}
	jo["companies"] = companies
	with open(OUTPUT_JSON_PATH, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"Saved: {OUTPUT_JSON_PATH}");


if __name__ == '__main__':
	main()
