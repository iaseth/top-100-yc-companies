import fs from 'fs';

import axios from 'axios';
import companiesJson from './src/companies.json' assert { type: "json" };



const { companies } = companiesJson;
companies.forEach(company => {
	const ycdbHtmlPath = `cache/${company.codeName}.ycdb.html`;

	if (fs.existsSync(ycdbHtmlPath)) {
		console.log(`Found: ${ycdbHtmlPath}`);
	} else {
		axios.get(company.pageURL).then(res => {
			fs.writeFileSync(ycdbHtmlPath, res.data, "utf8");
			console.log(`Saved: ${ycdbHtmlPath}`);
		})
	}
});
