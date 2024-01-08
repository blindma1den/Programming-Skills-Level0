import { useNavigate } from 'react-router'
import { useState } from 'react'
import bank from './assets/bitmap.png'

function App() {
	const [earn, setEarn] = useState(0)
	const [medical, setMedical] = useState(0)
	const [houseHOld, setHouseHOld] = useState(0)
	const [leisure, setLeisure] = useState(0)
	const [savings, setSavings] = useState(0)
	const [education, setEducation] = useState(0)

	const handleEarn = e => {
		const val = Number(e.target.value)
		setEarn(earn + val)
	}
	const handleMedical = e => {
		const val = Number(e.target.value)
		setMedical(medical + val)
	}
	const handleHousehold = e => {
		const val = Number(e.target.value)
		setHouseHOld(houseHOld + val)
	}
	const handleLeisure = e => {
		const val = Number(e.target.value)
		setLeisure(leisure + val)
	}
	const handleSavings = e => {
		const val = Number(e.target.value)
		setSavings(savings + val)
	}
	const handleEducation = e => {
		const val = Number(e.target.value)
		setEducation(education + val)
	}
	const handleSubmit = e => {
		e.preventDefault()
		e.target.previousSibling.value = ''
	}
	const handleCalculate = () => {
		const TOTAL_EXPENSES = medical + houseHOld + leisure + savings + education
		if (TOTAL_EXPENSES <= earn) {
			alert('congratulatios!, you are saving money')
		} else {
			const COMPARATE = [
				{ medical },
				{ houseHOld },
				{ leisure },
				{ savings },
				{ education },
			]

			const getHighVal = () => {
				let n = 0
				let s = ''
				COMPARATE.forEach(el => {
					const k = Number(Object.values(el))
					const v = String(Object.keys(el))
					if (n < k) {
						n = k
						s = v
					} else {
						console.log(': false')
					}
				})
				alert(`You should save money in ${s}, you are spending $${n}`)
			}

			getHighVal()
		}
	}

	return (
		<div className='flex flex-col  justify-center items-center bg-blue min-h-screen'>
			<div className='w-44'>
				<img className='w-full' src={bank} alt='' />
			</div>
			<div className=' w-[600px] text-center'>
				<h1 className='text-4xl mb-6 text-gray-100'>SAVING MANAGER SYSTEM</h1>
				<form
					id='form'
					className='flex w-full gap-x-2 h-11 justify-between items-center'
				>
					<label htmlFor='name' className='text-gray-100'>
						Earn
					</label>
					<div className='flex  w-[470px] gap-x-2'>
						<input
							type='text'
							name='earn'
							placeholder='Enter earnings'
							onChange={handleEarn}
							className='input-text grow'
						/>
						<button
							onClick={handleSubmit}
							className='text-gray-100 bg-cyan-600'
						>
							Add
						</button>
					</div>
				</form>
				<form
					action=''
					className='flex w-full gap-x-2 h-11 justify-between items-center'
				>
					<label htmlFor='pass' className='text-gray-100'>
						Medical expenses
					</label>
					<div className='flex  w-[470px] gap-x-2'>
						<input
							type='text'
							name='medical'
							placeholder='Enter Medical expenses'
							onChange={handleMedical}
							className='input-text grow'
						/>
						<button
							onClick={handleSubmit}
							className='text-gray-100 bg-cyan-600'
						>
							Add
						</button>
					</div>
				</form>
				<form
					action=''
					className='flex w-full gap-x-2 h-11 justify-between items-center'
				>
					<label htmlFor='pass' className='text-gray-100'>
						Household expenses
					</label>
					<div className='flex  w-[470px] gap-x-2'>
						<input
							type='text'
							name='household'
							placeholder='Enter Household'
							onChange={handleHousehold}
							className='input-text grow'
						/>

						<button
							onClick={handleSubmit}
							className='text-gray-100 bg-cyan-600'
						>
							Add
						</button>
					</div>
				</form>
				<form
					action=''
					className='flex w-full gap-x-2 h-11 justify-between items-center'
				>
					<label htmlFor='pass' className='text-gray-100'>
						Leisure
					</label>
					<div className='flex  w-[470px] gap-x-2'>
						<input
							type='text'
							name='leisure'
							placeholder='Enter leisure'
							onChange={handleLeisure}
							className='input-text grow'
						/>

						<button
							onClick={handleSubmit}
							className='text-gray-100 bg-cyan-600'
						>
							Add
						</button>
					</div>
				</form>
				<form
					action=''
					className='flex w-full gap-x-2 h-11 justify-between items-center'
				>
					<label htmlFor='pass' className='text-gray-100'>
						Savings
					</label>
					<div className='flex  w-[470px] gap-x-2'>
						<input
							type='text'
							name='savings'
							placeholder='Enter savings'
							onChange={handleSavings}
							className='input-text grow'
						/>

						<button
							onClick={handleSubmit}
							className='text-gray-100 bg-cyan-600'
						>
							Add
						</button>
					</div>
				</form>
				<form
					action=''
					className='flex w-full gap-x-2 h-11 justify-between items-center mb-4'
				>
					<label htmlFor='pass' className='text-gray-100'>
						Education
					</label>
					<div className='flex  w-[470px] gap-x-2'>
						<input
							type='text'
							name='education'
							placeholder='Enter education'
							onChange={handleEducation}
							className='input-text grow'
						/>
						<button
							onClick={handleSubmit}
							className='text-gray-100 bg-cyan-600'
						>
							Add
						</button>
					</div>
				</form>
				<button
					onClick={handleCalculate}
					className='text-gray-100 w-full bg-cyan-600'
				>
					Calculate
				</button>
			</div>
		</div>
	)
}

export default App
