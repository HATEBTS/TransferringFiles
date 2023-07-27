import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import DirectorySelectDialog from "./FileDialogButton";
// import './style/index.css';
// import './style/bootstrap.css';
import axios from 'axios'; //
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
  console.log(dataToSend)
  axios.post('http://127.0.0.1:5000/api/submit-form', dataToSend)
    .then((response) => {
      // Handle the server response here if needed
      console.log('Server response:', response.data);
    })
    .catch((error) => {
      // Handle errors here if needed
      console.error('Error while sending form data:', error);
    });
};

export default handleFormSubmit;