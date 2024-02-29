import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [tasks, setTasks] = useState([])
  const [newTask, setNewTask] = useState('')  
  const [gotNewTask, setGotNewTask] = useState(false)
  
  const baseURL = 'http://' // Add your server's IP address or domain here

  useEffect(() => {
    axios.get(baseURL + 'tasks/').then((res) => {
      setTasks(res.data)
      console.log(res.data)
    })
  }, [gotNewTask])

  const addTask = () => {
    if (newTask !== '') {
      axios.post(baseURL + 'tasks/create/', {task: newTask}).then((res) => {
        setTasks([...tasks, [res.data.id, newTask]])
        setGotNewTask(!gotNewTask)
      })
    }
  }
  const deleteTask = (id) => {
    axios.delete(baseURL + 'tasks/delete/?task_id=' + id).then((res) => {
      setGotNewTask(!gotNewTask)
    })
  }


  return (
    <>
      <div className='dark'>
        <div className='dark:bg-gray-900 bg-white h-screen flex flex-col items-center'>
          <h1 className='dark:text-white text-black text-3xl font-bold p-2'>EzTasklist</h1>
          <div className='border rounded-xl dark:border-gray-400 border-black w-2/3 lg:w-2/5 p-2'>
            <div className='flex justify-between'>
              <input type='text' onChange={(e) => setNewTask(e.target.value)} placeholder='Task here...' className='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-2/3 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'/>
              <button className='bg-blue-500 rounded-xl p-3 w-1/4 hover:bg-blue-600 text-white' onClick={addTask}>Submit</button>
            </div>
            
            <hr className='h-px my-4 bg-black dark:bg-gray-400 border-0'></hr>
            
            {
              tasks.length > 0?
                tasks.map((task, id) => (
                  <div className='flex bg-slate-700 m-2 p-3  items-center text-lg'>
                    <input id="checked-checkbox" onChange={() => deleteTask(task[0])} value={task[0]} type="checkbox" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"/>
                    <p className='ml-2 text-gray-200'>{task[1]}</p>
                  </div>
                ))
              : <div className='text-center text-gray-200'>No tasks available</div>
            }   
          </div>
        </div>
      </div>
    </>
  )
}

export default App
