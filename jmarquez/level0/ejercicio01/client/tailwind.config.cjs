/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./index.html', './src/**/*.{js,jsx}'],
	theme: {
		extend: {
			fontFamily: {
				primaria: ['Oswald', 'sans-serif'],
				secundaria: ['Rajdhani', 'sans-serif'],
			},
			colors: {
				blue: ' #054472 ',
				fleld: '#062b47',
			},
		},
	},
	variants: {
		textColor: ['responsive', 'hover', 'group-hover'],
		backgroundColor: ['responsive', 'hover', 'group-hover'],
		input: ['responsive'],
		div: ['responsive'],
	},

	plugins: [],
}
