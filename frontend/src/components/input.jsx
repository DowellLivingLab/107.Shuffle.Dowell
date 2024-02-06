import React, { useState } from 'react';

const MultiLineInput = ({onChange,  value, placeholder }) => {

  return (
 
        <textarea
        //   rows={4} // You can adjust the number of rows as needed
        //   cols={50} // You can adjust the number of columns as needed
        className='w-[400px] h-[485px] resize-none rounded-md p-2 bg-slate-100'
          value={value}
          onChange={onChange}
          placeholder= {placeholder}
        />

  );
};

export default MultiLineInput;
