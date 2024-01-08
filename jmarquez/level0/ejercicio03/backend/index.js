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
const PROGRAMS = {
	computer: [],
	medicine: [],
	marketing: [],
	arts: [],
};
const SLOT_CAMPUS = [
	{
		london: [
			{ program: 'computer', slot: 0 },
			{ program: 'marketing', slot: 0 },
			{ program: 'medicine', slot: 0 },
			{ program: 'arts', slot: 0 },
		],
		manchester: [
			{ program: 'computer', slot: 0 },
			{ program: 'marketing', slot: 0 },
			{ program: 'medicine', slot: 0 },
			{ program: 'arts', slot: 0 },
		],
		liverpool: [
			{ program: 'computer', slot: 0 },
			{ program: 'marketing', slot: 0 },
			{ program: 'medicine', slot: 0 },
			{ program: 'arts', slot: 0 },
		],
	},
];
let campusAvaliable = ['london', 'manchester', 'liverpool'];

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
APP.post('/register', (req, res) => {
	const { program, campus } = req.body;
	for (const i in PROGRAMS) {
		if (i == program) {
			PROGRAMS[i].push(req.body);
		}
		if (PROGRAMS[i].length > 5) {
			return res.send({ msg: 'program full', code: 400 });
		} else {
			for (let j = 0; j < SLOT_CAMPUS[0][campus].length; j++) {
				if (SLOT_CAMPUS[0][campus][j]['program'] == program) {
					if (SLOT_CAMPUS[0]['london'][j]['slot'] >= 1) {
						campusAvaliable.indexOf('london') !== -1 &&
							campusAvaliable.splice(campusAvaliable.indexOf('london'), 1);
						break;
					}
					if (SLOT_CAMPUS[0]['manchester'][j]['slot'] >= 3) {
						campusAvaliable.indexOf('manchester') !== -1 &&
							campusAvaliable.splice(campusAvaliable.indexOf('manchester'), 1);
						break;
					}
					if (SLOT_CAMPUS[0]['liverpool'][j]['slot'] >= 1) {
						campusAvaliable.indexOf('liverpool') !== -1 &&
							campusAvaliable.splice(campusAvaliable.indexOf('liverpool'), 1);
						break;
					}
					return (
						SLOT_CAMPUS[0][campus][j]['slot']++ &
						res.send({ msg: 'register succesfull', code: 200 })
					);
				}
			}
		}
	}
	res.send({
		msg: 'campus full, slots avaliable in: ' + campusAvaliable.join(' '),
		code: 400,
	});
});

APP.listen(PORT, () => {
	console.log(`running on port: ${PORT} `);
});
