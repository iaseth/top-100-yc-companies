import fs from 'fs';
import url from 'url';

import axios from 'axios';
import * as cheerio from 'cheerio';



const TOP_100_LINK = "https://www.ycdb.co/top-companies/alexa-rank";
const OUTPUT_JSON_PATH = "src/companies.json";

async function main () {
	const html = await axios.get(TOP_100_LINK).then(res => res.data);
	const $ = await cheerio.load(html);
	const companies = [];
	$("#table > tbody > tr").each((i, tr) => {
		const row = [];
		$(tr).find("td").each((i, td) => {
			const tdText = $(td).text().trim();
			row.push(tdText);
		});

		const relativeURL = $(tr).find("a").attr("href");
		const absoluteURL = url.resolve(TOP_100_LINK, relativeURL);

		const company = {};
		company.rank = parseInt(row[0]);
		company.name = row[1];
		company.batch = row[2];
		company.category = row[3];
		company.description = row[4];
		company.alexaRank = parseInt(row[5]);
		company.pageURL = absoluteURL;
		companies.push(company);
	});

	const jo = {companies};
	const jsonText = JSON.stringify(jo, null, '\t');
	fs.writeFileSync(OUTPUT_JSON_PATH, jsonText, "utf8");
	console.log(`Saved: ${OUTPUT_JSON_PATH}`);
}

main();
