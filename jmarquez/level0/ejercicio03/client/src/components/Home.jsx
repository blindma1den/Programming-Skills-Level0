/* eslint-disable react/prop-types */
import React, { useState } from 'react'
import { useNavigate } from 'react-router'
import bank from '../assets/bitmap.png'

export const Home = ({ setData }) => {
	const navigate = useNavigate()
	const [user, setUser] = useState('')
	const [pass, setPass] = useState('')
	const handleUser = e => {
		setUser(e.target.value)
	}
	const handlePass = e => {
		setPass(e.target.value)
	}
	const handleSubmit = async e => {
		e.preventDefault()

		fetch('http://localhost:5000/login', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				user,
				pass,
			}),
		})
			.then(res => res.json())
			.then(res => {
				if (res.code !== 200) return alert(res.msg)
				setData(res)
				navigate('/dashboard')
			})
	}

	return (
		<div className='flex flex-col justify-center items-center bg-blue min-h-screen'>
			<div className='w-52'>
				<img className='w-full' src={bank} alt='' />
			</div>
			<h1 className='text-4xl mb-6 text-gray-100'>
				UNIVERSITY ENROLLMENT SYSTEM
			</h1>
			<form action='' className=' w-72'>
				<div className='flex justify-between mb-4 items-center'>
					<label htmlFor='name' className='text-gray-100'>
						User
					</label>
					<input
						type='text'
						name='name'
						placeholder='Enter user'
						onChange={handleUser}
						className='input-text'
					/>
				</div>
				<div className='flex justify-between items-center mb-4'>
					<label htmlFor='pass' className='text-gray-100'>
						Password
					</label>
					<input
						type='password'
						name='pass'
						placeholder='Enter password'
						onChange={handlePass}
						className='input-text'
					/>
				</div>
				<button onClick={handleSubmit} className='text-gray-100 bg-cyan-600'>
					Login
				</button>
			</form>
		</div>
	)
}
