import companiesJson from './companies.json';



export interface CompanyType {
	rank: number,
	name: string,
	batch: string,
	category: string,
	description: string,
	alexaRank: number,
	pageURL: string,
}

export const companies: CompanyType[] = companiesJson.companies;
