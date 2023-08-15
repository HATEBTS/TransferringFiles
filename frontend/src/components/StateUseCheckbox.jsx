import React, { useState } from 'react';
import InfoTime from "./InfoTime";

function CheckBox() {
  const [isChecked, setIsChecked] = useState(false);

  const handleCheckboxChange = () => {
    setIsChecked(!isChecked);
  };

  return (
    <div className={"input-group cs-form d-flex justify-content-between mt-0 mx-auto w-50"}>

      <div className={"input-group-text pe-1 p-1 mt-2"}>
        <input
          className={"transparent-input form-check-input p-1 mt-0"}
          id={"flag"}
          type={"checkbox"}
          aria-label="Флажок для следующего ввода текста"
          onChange={handleCheckboxChange}
        />
      </div>
      <input
          name={"timeObed"}
        id={"inp1"}
        type="time"
        style={{ width: "60px" }}
        className={`p-1 mt-2 mx-auto form-control ${!isChecked ? "disabled" : ""}`}
        disabled={!isChecked}
      />
        <InfoTime />

    </div>
  );
}

export default CheckBox;