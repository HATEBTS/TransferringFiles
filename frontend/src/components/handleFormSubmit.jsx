import React from 'react';
import axios from 'axios';
import ErrorModal from "../errors/ErrorDate"; //
const handleFormSubmit = (event) => {
  event.preventDefault(); // Prevent the default form submission behavior

  // Collect the form data
  const formData = new FormData(event.target);
  const date = formData.get('date');
  const numberCamera = formData.get('number-camera');
  const numberObject = formData.get('number-object');
  const selectedPath = document.getElementById('selectedPath').value; // Get the selected path from the hidden input

  // Create an object with the form data to send to the server
  const dataToSend = {
    date,
    numberCamera,
    numberObject,
    selectedPath,
  };

  // Send the form data to the server using Axios or another HTTP library
  axios.post('http://127.0.0.1:5000/api/submit-form', dataToSend)
    .then((response) => {
      // Handle the server response here if needed
      console.log('Server response:', response.data);
    })
    .catch((error) => {
      if (error.response.data.date) {
      // Handle errors here if needed

        console.error('Error while sending form date:', error.response.data.date);
        alert("Вредная дата!")}
      else if (error.response.data.selectedPath){
        console.error('Error while sending form path:', error.response.data.date);
        alert("Вредный путь, выбери папку!")

      }
    });
};

export default handleFormSubmit;