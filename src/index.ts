import palettesJson from './palettes.json';



export interface CompanyType {
	rank: number,
	name: string,

	codeName: string,
	jsonName: string,
	pngName: string,
	metaJsonName: string,

	batch: string,
	category: string,
	description: string,
	alexaRank: number,
	pageURL: string,

	metaJsonPath: string,
	logoPngPath: string,
	palettePngPath: string,
	hexPalette: string[],
}

export const companies: CompanyType[] = palettesJson.palettes;
