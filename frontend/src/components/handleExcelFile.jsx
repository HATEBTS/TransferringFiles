import React, { useState } from 'react';
import axios from 'axios';

const ApiCallButton = () => {
  const [isLoading, setIsLoading] = useState(false);

  const handleApiCall = async () => {
    try {
      setIsLoading(true);

      // Вызов API
      const response = await axios.get('http://127.0.0.1:5000/download_excel'); // Замените на реальный URL вашего API

      // Обработка ответа от API
      console.log('Ответ от API:', response.data);

      setIsLoading(false);
    } catch (error) {
      console.error('Ошибка вызова API:', error);
      setIsLoading(false);
    }
  };

  return (
    <div>
      <button className={"btn btn-dark"} onClick={handleApiCall} disabled={isLoading}>
        {isLoading ? 'Загрузка...' : 'Выгрузить'}
      </button>
    </div>
  );
};

export default ApiCallButton;