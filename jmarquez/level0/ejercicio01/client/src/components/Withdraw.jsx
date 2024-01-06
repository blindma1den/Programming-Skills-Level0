/* eslint-disable react/prop-types */
import React, { useState } from 'react'

const Withdraw = ({ data, setData }) => {
	const [deposit, setDeposit] = useState(0)
	const { nam } = data
	console.log(nam)
	const handleWithdrawAmount = e => {
		setDeposit(e.target.value)
	}
	const handleWithdrawSubmit = e => {
		e.preventDefault()
		fetch('http://localhost:5000/withdraw', {
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
			<form action=''>
				<button onClick={handleWithdrawSubmit} className='bg-red-400 mr-4'>
					Withdraw
				</button>
				<input
					type='number'
					name=''
					id=''
					placeholder='amount to deposit'
					onChange={handleWithdrawAmount}
					required
					className='input-text'
				/>
			</form>
		</div>
	)
}

export default Withdraw
