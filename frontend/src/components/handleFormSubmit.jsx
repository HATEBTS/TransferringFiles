import React, { useState } from 'react';
import axios from 'axios';
const handleFormSubmit = (event) => {
  event.preventDefault(); // Prevent the default form submission behavior
  const modal = document.getElementById("myModal");
  const btn = document.getElementById("btn");
  const closeBtn = document.getElementsByClassName("close")[0];

  // Collect the form data
  const formData = new FormData(event.target);
  const date = formData.get('date');
  const numberCamera = formData.get('number-camera');
  const numberObject = formData.get('number-object');
  const timeObed = formData.get('timeObed');
  const selectedPath = document.getElementById('selectedPath').value; // Get the selected path from the hidden input

  // Create an object with the form data to send to the server
  const dataToSend = {
    date,
    numberCamera,
    numberObject,
    selectedPath,
    timeObed
  };
  console.log(dataToSend)

  modal.style.display = "block";


  modal.style.display = "block";

  // Send the form data to the server using Axios or another HTTP library
  axios.post('http://127.0.0.1:5000/api/submit-form', dataToSend)
    .then((response) => {
      // Handle the server response here if needed

      console.log('Server response:', response.data);
      modal.style.display = "none";
      alert("Готово!")

    })
    .catch((error) => {
      if (error.response.data.date) {
      // Handle errors here if needed
      modal.style.display = "none";

        console.error('Error while sending form date:', error.response.data.date);
        alert("Вредная дата!")}
      else if (error.response.data.selectedPath){
        console.error('Error while sending form path:', error.response.data.selectedPath);
        alert("Вредный путь, выбери папку!")
        modal.style.display = "none";


      }
      else if (error.response.data.Napas_lavandos){
        console.error('Error while sending form file:', error.response.data.Napas_lavandos);
        alert("Нету файлов, выбери папку!")
        modal.style.display = "none";


      }
      else if (error.response.data.NoDateFile){
        console.error('Error while sending form date plus file:', error.response.data.NoDateFile);
        alert("Нет файлов соответствующих дате!")
        modal.style.display = "none";


      }
    });
};

export default handleFormSubmit;