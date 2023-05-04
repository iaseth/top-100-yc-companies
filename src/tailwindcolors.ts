import coloria from "coloria";
import { companies } from "./company";

interface ObjectType {
	[key: string]: coloria.TailwindColor
}

export const tailwindcolors: ObjectType = {};

companies.forEach(company => {
	company.hexPalette.forEach((hex, idx) => {
		const colorName = idx ? `${company.codeName}-${idx}` : company.codeName;
		const color = coloria.fromHex(hex, colorName);
		if (color) {
			tailwindcolors[colorName] = color.getTailwindPalette();
		}
	});
});
