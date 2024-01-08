/* eslint-disable react/prop-types */
import React, { useState } from 'react'
import { Outlet, useNavigate } from 'react-router'

const Dashboard = ({ data, setData }) => {
	const navigate = useNavigate()
	const [senderName, setSenderName] = useState('')
	const [senderLastName, setSenderLastName] = useState('')
	const [recipientName, setRecipientName] = useState('')
	const [recipientLastName, setRecipientLastName] = useState('')
	const [address, setAddress] = useState('')
	const [weight, setWeight] = useState(0)
	const [pay, setPay] = useState(0)

	const handleSenderName = e => {
		setSenderName(e.target.value)
	}
	const handleSenderLastName = e => {
		setSenderLastName(e.target.value)
	}
	const handleRecipientName = e => {
		setRecipientName(e.target.value)
	}
	const handleRecipientLastName = e => {
		setRecipientLastName(e.target.value)
	}
	const handleAddress = e => {
		setAddress(e.target.value)
	}
	const handleWeight = e => {
		const INITIAL_VAL = e.target.value
		setWeight(INITIAL_VAL)
		setPay(INITIAL_VAL * 2)
	}

	const handleSubmit = e => {
		e.preventDefault()

		const nextOpertaion = confirm(`
			Package sent to: ${recipientName} ${recipientLastName}
			Address: ${address}
			TOTAL TO PAY: $${pay}
			Do you want to do another operation?
			
		`)
		if (!nextOpertaion) {
			setData({})
			navigate('/')
		}
	}
	return (
		<div className='flex flex-col justify-center items-center bg-blue min-h-screen'>
			<h1 className='text-6xl mb-5'>{data.nam}</h1>
			<p className='text-3xl mb-4'>WELCOME!</p>
			<form action=''>
				<h1>Sender info</h1>
				<div className='flex bg-fleld py-4 px-2 w-72 justify-between '>
					<label htmlFor='name'>Name</label>
					<input
						className='mr-2 bg-transparent text-gray-200'
						type='text'
						id='name'
						name='nanme'
						placeholder='Insert your name'
						onChange={handleSenderName}
					/>
				</div>
				<div className='flex bg-fleld py-4 px-2 w-72 justify-between mb-4'>
					<label htmlFor='lastname'>Lastname</label>
					<input
						className='mr-2 bg-transparent text-gray-200'
						type='text'
						id='lastname'
						name='lastname'
						placeholder='Insert your lastname'
						onChange={handleSenderLastName}
					/>
				</div>
				<h1>Recipient info</h1>
				<div className='flex bg-fleld py-4 px-2 w-72 justify-between '>
					<label htmlFor='name'>Name</label>
					<input
						className='mr-2 bg-transparent text-gray-200'
						type='text'
						id='recipientName'
						name='recipientName'
						placeholder='Insert recipient name'
						onChange={handleRecipientName}
					/>
				</div>
				<div className='flex bg-fleld py-4 px-2 w-72 justify-between'>
					<label htmlFor='lastname'>Lastname</label>
					<input
						className='mr-2 bg-transparent text-gray-200'
						type='text'
						id='recipientLastname'
						name='recipientLastname'
						placeholder='Insert recipient lastname'
						onChange={handleRecipientLastName}
					/>
				</div>
				<div className='flex bg-fleld py-4 px-2 w-72 justify-between'>
					<label htmlFor='lastname'>Address</label>
					<input
						className='mr-2 bg-transparent text-gray-200'
						type='text'
						id='address'
						name='address'
						placeholder='Insert recipient address'
						onChange={handleAddress}
					/>
				</div>
				<div className='flex bg-fleld py-4 px-2 w-72 justify-between mb-2'>
					<label htmlFor='lastname'>weight</label>
					<input
						className='mr-2 bg-transparent text-gray-200'
						type='number'
						id='weight'
						name='weight'
						placeholder='Insert weight in klg'
						onChange={handleWeight}
					/>
				</div>
				<p className='mb-4'>amount to pay: ${pay}</p>

				<button
					className='bg-green-700 w-full hover:bg-green-900'
					onClick={handleSubmit}
				>
					Submit
				</button>
			</form>
			{/* <ul className='flex justify-center mb-4 gap-4'>
				<li>
					<NavLink to='convert'>Convert</NavLink>
				</li>
				<li>
					<NavLink to='withdraw'>Withdraw</NavLink>
				</li>
			</ul> */}
			<div>
				<Outlet />
			</div>
		</div>
	)
}

export default Dashboard
