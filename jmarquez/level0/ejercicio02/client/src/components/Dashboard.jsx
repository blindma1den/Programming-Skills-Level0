/* eslint-disable react/prop-types */
import React from 'react'
import { Outlet } from 'react-router'
import { NavLink } from 'react-router-dom'

const Dashboard = ({ data }) => {
	return (
		<div className='flex flex-col justify-center items-center bg-blue min-h-screen'>
			<h1 className='text-6xl mb-5'>{data.nam}</h1>
			<p className='text-3xl mb-4'>
				Currency: {data.currency} {data.amount}{' '}
			</p>
			<ul className='flex justify-center mb-4 gap-4'>
				<li>
					<NavLink to='convert'>Convert</NavLink>
				</li>
				<li>
					<NavLink to='withdraw'>Withdraw</NavLink>
				</li>
			</ul>
			<div>
				<Outlet />
			</div>
		</div>
	)
}

export default Dashboard
