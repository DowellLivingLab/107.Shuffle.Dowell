import React, { useState } from 'react';
import MultiLineInput from './components/input';
import shuffleData from './client/shuffle';

function App() {
  const [output, setOutput] = useState([]);
  const [input, setInput] = useState('');

  const handleMultiLineInputChange = (change) => {
    setInput(change.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault()
    const data = input.split(",").map((item) => item.trim());
    const shuffle = await shuffleData(data);
    setOutput([...shuffle]);


  };

  return (
    <div className='grid place-content-center bg-blue-400 max-h-screen'>
        <div className='m-4 p-4 max-w-[1000px] flex flex-col h-screen'>
          <div className='m-4 pt-4 h-24 text-center'>
            <h1 className='text-4xl text-white font-extrabold'>Shuffle API</h1>
          </div>
          <div className='m-4 pt-4 flex justify-around w-full h-3/4'>
            <form className='w-[400px]' onSubmit={handleSubmit}>
              <MultiLineInput
                onChange={handleMultiLineInputChange}
                // value={multiLineText}
                placeholder={"Input your data"}
              />
              <div className='grid place-content-center m-4'>
                  <button className='w-[400px] h-12 bg-blue-500 text-white rounded-md shadow-lg'>
                    Shuffle
                  </button>
              </div>
            </form>

            <div className='bg-slate-100 w-[400px] h-full rounded-md p-2'>
              <p className='text-gray-500'>Output</p>
              {
                output.map((item, index)=>{
                  return <p className="p-4 border-b-gray-200 text-center text-gray-400 text-bold font-semibold"key={index}>{item}</p>
                })
              }
          
            </div>
          </div>
        </div>

    </div>
  )

  }
export default App
