import { Route, Routes } from 'react-router'
import { Home } from './components/Home'
import { useState } from 'react'
import Dashboard from './components/Dashboard'
import Transfer from './components/Transfer'
import Deposit from './components/Deposit'
import Withdraw from './components/Withdraw'
function App() {
	const [data, setData] = useState({})
	return (
		<div className='h-full flex flex-col max-h-full flex-grow text-center'>
			<Routes>
				<Route path='/' element={<Home setData={setData} />} />
				<Route path='/dashboard' element={<Dashboard data={data} />}>
					<Route
						path='transfer'
						element={<Transfer data={data} setData={setData} />}
					/>
					<Route
						path='deposit'
						element={<Deposit data={data} setData={setData} />}
					/>
					<Route
						path='withdraw'
						element={<Withdraw data={data} setData={setData} />}
					/>
				</Route>
			</Routes>
		</div>
	)
}

export default App
