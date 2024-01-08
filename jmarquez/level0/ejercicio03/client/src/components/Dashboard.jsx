/* eslint-disable react/prop-types */
import React, { useState } from 'react'

const Dashboard = ({ data }) => {
	const [name, setName] = useState('')
	const [lastName, setLastName] = useState('')
	const [program, setProgram] = useState('')
	const [campus, setCampus] = useState('')

	const handleName = e => {
		setName(e.target.value)
	}
	const handleLastName = e => {
		setLastName(e.target.value)
	}
	const handleCampus = e => {
		setCampus(e.target.value)
	}
	const handleProgram = e => {
		setProgram(e.target.value)
	}

	const handleSubmit = e => {
		e.preventDefault()

		fetch('http://localhost:5000/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				name,
				lastName,
				program,
				campus,
			}),
		})
			.then(res => res.json())
			.then(res => {
				if (res.code === 200) {
					return alert(res.msg)
				}

				if (res.code === 400) return alert(res.msg)
			})
	}
	return (
		<div className='flex flex-col justify-center items-center bg-blue min-h-screen'>
			<h1 className='text-6xl mb-5'>{data.nam}</h1>
			<p className='text-3xl mb-4'>WELCOME!</p>
			<form action=''>
				<div className='flex bg-fleld py-4 px-2 w-72 justify-between '>
					<label htmlFor='name'>Name</label>
					<input
						className='mr-2 bg-transparent text-gray-200'
						type='text'
						id='name'
						name='nanme'
						placeholder='Insert your name'
						onChange={handleName}
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
						onChange={handleLastName}
					/>
				</div>
				<fieldset className='flex flex-col gap-y-5 mb-2'>
					<legend className='text-2xl mb-2'>Select your program:</legend>
					<div className='flex bg-fleld py-4 px-2 w-72 justify-between items-center'>
						<label htmlFor=''>Campus</label>
						<select
							name=''
							id=''
							onChange={handleCampus}
							className='bg-fleld border border-gray-300 text-gray-200 text-sm rounded-lg focus:ring-blue-500  focus:border-blue-500 block w-48 p-2.5'
						>
							<option defaultValue='london'>london</option>
							<option defaultValue='manchester'>manchester</option>
							<option defaultValue='liverpool'>liverpool</option>
						</select>
					</div>

					<div className='flex bg-fleld py-4 px-2 w-72'>
						<input
							className='mr-2'
							type='radio'
							id='computer'
							name='drone'
							value='computer'
							onChange={handleProgram}
						/>
						<label htmlFor='computer'>Computer Science</label>
					</div>

					<div className='flex bg-fleld py-4 px-2 w-72'>
						<input
							className='mr-2'
							type='radio'
							id='medicine'
							name='drone'
							value='medicine'
							onChange={handleProgram}
						/>
						<label htmlFor='medicine'>Medicine</label>
					</div>

					<div className='flex bg-fleld py-4 px-2 w-72'>
						<input
							className='mr-2'
							type='radio'
							id='marketing'
							name='drone'
							value='marketing'
							onChange={handleProgram}
						/>
						<label htmlFor='marketing'>Marketing</label>
					</div>
					<div className='flex bg-fleld py-4 px-2 w-72'>
						<input
							className='mr-2'
							type='radio'
							id='arts'
							name='drone'
							value='arts'
							onChange={handleProgram}
						/>
						<label htmlFor='arts'>Arts</label>
					</div>
				</fieldset>
				<button
					className='bg-cyan-700 w-full hover:bg-cyan-900'
					onClick={handleSubmit}
				>
					Submit
				</button>
			</form>
		</div>
	)
}

export default Dashboard
