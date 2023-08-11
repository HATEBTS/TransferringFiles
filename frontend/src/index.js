import React from 'react';
import ReactDOM from 'react-dom/client';
import './style/index.css';
import './style/bootstrap.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePages from "./components/HomePage";
import BaseWork from "./components/WindowBaseWork";
import ApiCallButton from "./components/handleExcelFile";
import LoadingModal from "./components/ModalLoading";
import CheckBox from "./components/StateUseCheckbox";




const elements = (
    <div>
      <Router>
        <Routes>
            <Route path="/" element={<HomePages />} />
            <Route path="/home" element={<HomePages />} />
            <Route path="/base" element={<BaseWork />} />
        </Routes>
      </Router>
    </div>
)
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(elements);
