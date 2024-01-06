/* eslint-disable react/prop-types */
import React, { useState } from 'react'

const Transfer = ({ data, setData }) => {
	const [deposit, setDeposit] = useState(0)
	const [name, setName] = useState('')
	const { nam } = data
	console.log(nam)
	const handleTransferAmount = e => {
		setDeposit(e.target.value)
	}
	const handleName = e => {
		e.preventDefault()
		setName(e.target.value)
	}
	const handleTransferSubmit = e => {
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
			.then(res => {
				setData(res)
				alert(`transfer to ${name} completed successfully`)
			})
	}
	return (
		<div>
			<form action='' className='flex flex-col'>
				<input
					type='text'
					placeholder='Insert name'
					onChange={handleName}
					className='input-text mb-4'
				/>
				<input
					type='number'
					name=''
					id=''
					placeholder='amount to deposit'
					onChange={handleTransferAmount}
					required
					className='input-text mb-4'
				/>
				<button onClick={handleTransferSubmit} className='bg-red-400'>
					Transfer
				</button>
			</form>
		</div>
	)
}

export default Transfer
