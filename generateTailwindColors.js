const fs = require('fs');

const coloria = require('coloria');
const palettesJson = require('./src/palettes.json');

const { palettes } = palettesJson;

const tailwindcolors = {};
palettes.forEach(company => {
	company.hexPalette.forEach((hex, idx) => {
		const colorName = idx ? `${company.codeName}-${idx}` : company.codeName;
		const color = coloria.fromHex(hex, colorName);
		if (color) {
			tailwindcolors[colorName] = color.getTailwindPalette();
		}
	});
});

const outputJsonPath = "src/tailwindcolors.json";
fs.writeFileSync(outputJsonPath, JSON.stringify(tailwindcolors, null, "\t"));
console.log(`Saved: ${outputJsonPath}`);
