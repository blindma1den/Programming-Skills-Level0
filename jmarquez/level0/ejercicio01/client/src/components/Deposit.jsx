/* eslint-disable react/prop-types */
import { useState } from 'react'

const Deposit = ({ data, setData }) => {
	const [deposit, setDeposit] = useState(0)
	const { nam } = data
	console.log(nam)
	const handleDepositAmount = e => {
		setDeposit(e.target.value)
	}
	const handleDepositSubmit = e => {
		e.preventDefault()
		fetch('http://localhost:5000/deposit', {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				deposit,
				nam,
			}),
		})
			.then(res => res.json())
			.then(res => setData(res))
	}
	return (
		<div>
			<form className=' flex justify-center items-center'>
				<button onClick={handleDepositSubmit} className='bg-green-400 mr-5'>
					Deposit
				</button>
				<input
					type='number'
					name=''
					id=''
					placeholder='amount to deposit'
					onChange={handleDepositAmount}
					className='input-text'
					required
				/>
			</form>
		</div>
	)
}

export default Deposit
