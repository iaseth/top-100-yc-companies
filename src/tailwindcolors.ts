import tailwindcolorsJson from './tailwindcolors.json';


export interface TailwindColor {
	"50": string,
	"100": string,
	"200": string,
	"300": string,
	"400": string,
	"500": string,
	"600": string,
	"700": string,
	"800": string,
	"900": string,
	"950": string,
}

interface ObjectType {
	[key: string]: TailwindColor
}

export const tailwindcolors: ObjectType = tailwindcolorsJson;
