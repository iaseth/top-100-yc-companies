import companiesJson from './companies.json';



export interface CompanyType {
	rank: number,
	name: string,
	codeName: string,
	jsonName: string,
	batch: string,
	category: string,
	description: string,
	alexaRank: number,
	pageURL: string,
}

export const companies: CompanyType[] = companiesJson.companies;
