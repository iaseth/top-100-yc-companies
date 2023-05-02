import companiesJson from './companies.json';



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
}

export const companies: CompanyType[] = companiesJson.companies;
