import React, { useState } from 'react';
import axios from 'axios';

const SheetsG = () => {
  const [isLoading, setIsLoading] = useState(false);

  const handleApiCall = async () => {
    try {
      setIsLoading(true);

      // Вызов API
      const response = await axios.get('http://127.0.0.1:5000/google_sheets');

      // Обработка ответа от API
      console.log('Ответ от API:', response.data);

      setIsLoading(false);
    } catch (error) {
      console.error('Ошибка вызова API:', error);
      alert("Ошибка", error);
      setIsLoading(false);
    }
  };

  return (
        <div className={"row align-items-start"}>
          <div className={"col"}>
            <button className={"btn btn-dark"} onClick={handleApiCall} disabled={isLoading}>
              {isLoading ? 'Загрузка...' : 'Обновить Гугл таблицу'}
            </button>
          </div>
        </div>
  );
};

export default SheetsG;