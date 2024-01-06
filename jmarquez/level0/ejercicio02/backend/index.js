import express from 'express';
import cors from 'cors';
import bodyParser from 'body-parser';
const APP = express();
const PORT = 5000;

const users = [
	{
		nam: 'jon',
		pass: '123',
	},
	{
		nam: 'Kate Wong',
		pass: '@PASSujhp',
	},
];
const coins = {
	CLP: {
		MIN: 10000,
		MAX: 1000000,
		ARS: 0.91,
		USD: 0.0011,
		EUR: 0.001,
		TRY: 0.033,
		GBP: 0.00088,
	},
	ARS: {
		MIN: 200000,
		MAX: 2000000,
		CLP: 1.1,
		USD: 0.0012,
		EUR: 0.0011,
		TRY: 0.037,
		GBP: 0.00097,
	},
	USD: {
		MIN: 10,
		MAX: 1000,
		CLP: 888.94,
		ARS: 811.2,
		EUR: 0.91,
		TRY: 29.82,
		GBP: 0.79,
	},
	EUR: {
		MIN: 5,
		MAX: 1000,
		CLP: 974.06,
		ARS: 888.87,
		USD: 1.1,
		TRY: 32.68,
		GBP: 0.86,
	},
	TRY: {
		MIN: 15,
		MAX: 2000,
		CLP: 29.81,
		ARS: 27.2,
		USD: 0.034,
		EUR: 0.031,
		GBP: 0.026,
	},
	GBP: {
		MIN: 10,
		MAX: 3000,
		CLP: 1131.18,
		ARS: 1032.25,
		USD: 1.27,
		EUR: 1.16,
		TRY: 37.95,
	},
};

let logTry = 3;
APP.use(express());
APP.use(cors());
APP.use(bodyParser.urlencoded({ extended: true }));
APP.use(bodyParser.json());

APP.get('/', (req, res) => {
	return;
});
APP.post('/login', (req, res) => {
	if (req.method !== 'POST') return;
	const USER = req.body.user;
	const PASS = req.body.pass;

	if (logTry === 1)
		return res.status(401).send({ msg: 'System blocked', code: 401 });
	const USER_AUTH = users.filter(user => user.nam == USER);
	const PASS_AUTH = USER_AUTH.filter(user => user.pass == PASS);
	if (USER_AUTH.length == 0 || PASS_AUTH.length == 0) {
		logTry--;
		return res.status(401).send({
			msg: `User or password not found, tries remaining: ${logTry}`,
			code: 401,
			try: logTry,
		});
	}
	delete USER_AUTH[0].pass;
	res.status(200).send({ ...USER_AUTH[0], code: 200 });
});
APP.post('/convert', (req, res) => {
	const { fromCurrency, toCurrency, amount } = req.body;

	let amountConverted;
	let parsedAmount;
	for (const CURRENCY in coins) {
		if (CURRENCY == fromCurrency) {
			const MIN = coins[CURRENCY]['MIN'];
			const MAX = coins[CURRENCY]['MAX'];
			if (amount < MIN)
				return res.status(401).send({
					msg: `Amount to convert cannot be minus than ${CURRENCY}${MIN} `,
					code: 401,
				});
			if (amount > MAX)
				return res.status(401).send({
					msg: `Amount to convert cannot be more than ${CURRENCY}${MAX} `,
					code: 401,
				});
			amountConverted = amount * coins[CURRENCY][toCurrency];
			parsedAmount = parseFloat(amountConverted).toFixed(2);
		}
	}
	res
		.status(200)
		.send({ currency: toCurrency, amount: parsedAmount, code: 200 });
});
APP.put('/withdraw', (req, res) => {
	const DEPOSIT = Number(req.body.deposit);
	const CURRENT_AMOUNT = req.body.amount;
	const NEW_AMOUNT = CURRENT_AMOUNT - DEPOSIT;
	const COMISSION = (NEW_AMOUNT * 1) / 100;
	req.body.amount = NEW_AMOUNT + COMISSION;
	res.status(200).send(req.body);
});

APP.listen(PORT, () => {
	console.log(`running on port: ${PORT} `);
});
