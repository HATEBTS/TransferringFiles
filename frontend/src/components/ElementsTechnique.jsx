import React from 'react';


function ElementsTechnique() {
   const arOptions = [];
   for (let i = 1; i < 11; i++) {
      arOptions.push("Звено " + i);
  // ещё какие-то инструкции
   }
    const transparentOptionStyles = {
    background: 'transparent',
    color: '#333',
  };
   const options = arOptions.map((text, index) => {
      return <option style={transparentOptionStyles} key={index}>{text}</option>;
   });
   const transparentSelectStyles = {
    background: 'transparent',
    border: '1px solid #ccc',
    padding: '8px',
    color: '#ffffff',
  };


  const transparentOptionStylesFirst = {
    background: 'transparent',
    color: '#333',
  };
   return <div>
      <select style={transparentSelectStyles} name={"number-camera"} className={"mt-2 mx-auto w-50 form-control form-control-sm p-1"} onChange={(event) => event.target.value}>
         <option style={transparentOptionStylesFirst}>Выберите звено</option>
         {options}
      </select>
   </div>;
}



export default ElementsTechnique;