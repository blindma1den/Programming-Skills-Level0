import { Route, Routes } from 'react-router'
import { Home } from './components/Home'
import { useState } from 'react'
import Dashboard from './components/Dashboard'
import Withdraw from './components/Withdraw'
import Convert from './components/Convert'
function App() {
	const [data, setData] = useState({})
	return (
		<div className='h-full flex flex-col max-h-full flex-grow text-center'>
			<Routes>
				<Route path='/' element={<Home setData={setData} />} />
				<Route path='/dashboard' element={<Dashboard data={data} />}>
					<Route
						path='convert'
						element={<Convert data={data} setData={setData} />}
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
