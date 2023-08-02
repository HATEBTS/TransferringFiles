import React, { useState } from 'react';
import { open} from "@tauri-apps/api/dialog";

const DirectorySelectDialog = ({ onSelect }) => {
  const [selectedPath, setSelectedPath] = useState('');

  const handleOpenDialog = async () => {
    try {
      const result = await open({
        directory: true, // Указываем, что нужно выбрать каталог, а не файл
      });
      if (result && result.length > 0) {
        setSelectedPath(result); // Сохраняем выбранный путь в состоянии компонента
        onSelect(result); // Вызываем колбэк, чтобы передать путь родительскому компоненту (или использовать его по своему усмотрению)
      }
      console.log(result)
    } catch (error) {
      console.error('Error while opening directory dialog:', error);
    }
  };

  return (
    <div>
      <button type="button" onClick={handleOpenDialog} className="mt-2 mx-auto form-control w-50 btn-primary">
        Выбрать каталог
      </button>
      <p className={"mt-2 mx-auto text-center"}>Выбранный путь: {selectedPath}</p>
    </div>
  );
};

export default DirectorySelectDialog;