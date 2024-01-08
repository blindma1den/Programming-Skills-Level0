/* eslint-disable react/prop-types */
import { useState } from 'react'
import { useNavigate } from 'react-router'

const Convert = ({ data, setData }) => {
	const navigate = useNavigate()
	const [amount, setAmount] = useState(0)
	const [fromCurrency, setFromCurrency] = useState('')
	const [toCurrency, setToCurrency] = useState('')
	const handleAmounttoCOnvert = e => {
		setAmount(e.target.value)
	}
	const handleFrom = e => {
		setFromCurrency(e.target.value)
	}
	const handleTo = e => {
		setToCurrency(e.target.value)
	}
	const handleDepositSubmit = e => {
		e.preventDefault()
		fetch('http://localhost:5000/convert', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				amount,
				fromCurrency,
				toCurrency,
			}),
		})
			.then(res => res.json())
			.then(res => {
				if (res.code === 200) {
					setData({ ...data, ...res })
					const CONTINUE = confirm('Do you want to do another transaction?')
					if (!CONTINUE) {
						setData({})
						navigate('/')
					}
				} else {
					alert(res.msg)
				}
			})
	}
	return (
		<div>
			<form className=' flex flex-col justify-center items-center gap-y-10'>
				<div className='flex gap-x-6'>
					<h2 className='text-gray-200 text-2xl'>Amount</h2>
					<input
						type='number'
						name=''
						id=''
						placeholder='amount to convert'
						onChange={handleAmounttoCOnvert}
						className='input-text'
						required
					/>
				</div>
				<div className='flex gap-x-10 justify-center '>
					<div className='flex gap-x-4'>
						<h3 className='text-gray-200 text-2xl'>From</h3>
						<select
							onChange={handleFrom}
							name=''
							id=''
							className='w-42 bg-fleld border border-gray-300 text-gray-200 text-sm rounded-lg focus:ring-blue-500  focus:border-blue-500 block w-full p-2.5 '
						>
							<option value='Select' selected>
								Select
							</option>
							<option value='ARS'>ARS</option>
							<option value='USD'>USD</option>
							<option value='CLP'>CLP</option>
							<option value='EUR'>EUR</option>
							<option value='TRY'>TRY</option>
							<option value='GBP'>GBP</option>
							<option value='USD'>USD</option>
						</select>
					</div>
					<div className='flex gap-x-4'>
						<h3 className='text-gray-200 text-2xl'>To</h3>
						<select
							onChange={handleTo}
							name=''
							id=''
							className='w-42 bg-fleld border border-gray-300 text-gray-200 text-sm rounded-lg focus:ring-blue-500  focus:border-blue-500 block w-full p-2.5 '
						>
							<option value='Select' selected>
								Select
							</option>
							<option value='ARS'>ARS</option>
							<option value='USD'>USD</option>
							<option value='CLP'>CLP</option>
							<option value='EUR'>EUR</option>
							<option value='TRY'>TRY</option>
							<option value='GBP'>GBP</option>
							<option value='USD'>USD</option>
						</select>
					</div>
				</div>
				<button onClick={handleDepositSubmit} className='bg-green-400 mr-5'>
					Convert
				</button>
			</form>
		</div>
	)
}

export default Convert
