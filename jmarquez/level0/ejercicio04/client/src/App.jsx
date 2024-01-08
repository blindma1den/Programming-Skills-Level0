import { Route, Routes } from 'react-router'
import { Home } from './components/Home'
import { useState } from 'react'
import Dashboard from './components/Dashboard'
import Send from './components/Send'

function App() {
	const [data, setData] = useState({})
	return (
		<div className='h-full flex flex-col max-h-full flex-grow text-center'>
			<Routes>
				<Route path='/' element={<Home setData={setData} />} />
				<Route
					path='/dashboard'
					element={<Dashboard data={data} setData={setData} />}
				>
					<Route path='send' element={<Send data={data} setData={setData} />} />
				</Route>
			</Routes>
		</div>
	)
}

export default App
