const button = document.querySelector(".button-dir")

button.addEventListener("click", function (){
     QFileDialog::getExistingDirectory(0, "Выбор папки", "");


})