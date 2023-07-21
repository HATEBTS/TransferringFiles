<<<<<<< HEAD
const { open } = window.__TAURI__.dialog;

function setupButton() {
  const openDialogBtn = document.getElementById('openDialogBtn');
  openDialogBtn.addEventListener('click', handleOpenDialogClick);
}

async function handleOpenDialogClick() {
  try {
    const result = await open({
      multiple: false, // Позволяет выбрать несколько файлов или папок
      directory: true, // Установите true, чтобы разрешить выбор только папок, а не файлов
      filter: 'All Files|*.*', // Фильтр файлов (например, 'Images|*.png;*.jpg;*.gif')
    });

    // result содержит путь(и) выбранных файлов или папок
    console.log(result);
  } catch (error) {
    console.error('Произошла ошибка при открытии диалогового окна: ', error);
  }
}

// Вызываем функцию для настройки обработчика кнопки после загрузки DOM
document.addEventListener('DOMContentLoaded', setupButton);

=======
const button = document.querySelector(".button-dir")

button.addEventListener("click", function (){
     QFileDialog::getExistingDirectory(0, "Выбор папки", "");


})
>>>>>>> 3e00a37255219eba0cd6c8c856a4774766c61dbb
