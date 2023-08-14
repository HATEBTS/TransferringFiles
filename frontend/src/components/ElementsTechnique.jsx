import React from 'react';


function ElementsTechnique() {
   const arOptions = [];
   for (let i = 1; i < 11; i++) {
      arOptions.push("Звено " + i);
  // ещё какие-то инструкции
   }

   const options = arOptions.map((text, index) => {
      return <option key={index}>{text}</option>;
   });

   return <div>
      <select name={"number-camera"} className={"mt-2 mx-auto w-50 form-control form-control-sm p-1 bg-light border"} onChange={(event) => event.target.value}>
         <option>Выберите звено</option>
         {options}
      </select>
   </div>;
}



export default ElementsTechnique;