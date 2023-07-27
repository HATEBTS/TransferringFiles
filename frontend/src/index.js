import React from 'react';
import ReactDOM from 'react-dom/client';
import './style/index.css';
import './style/bootstrap.css';
import DirectorySelectDialog from "./components/FileDialogButton";
import handleFormSubmit from "./components/handleFormSubmit";
// import App from './App';
// import reportWebVitals from './reportWebVitals';
const handleDirectorySelect = (selectedPath) => {
  console.log('Selected directory path:', selectedPath);
  const selectedPathInput = document.getElementById('selectedPath');
    selectedPathInput.value = selectedPath;
  // Do whatever you want to do with the selected path here
};

const elements = (<div className="name">
    <div className={"container center-block"}>
        <form id={"form"} method={"post"} action={"http://localhost:5000/api/submit-form"} onSubmit={handleFormSubmit} target={"_blank"}>

                <DirectorySelectDialog onSelect={handleDirectorySelect} />
                <input type={"hidden"} id={"selectedPath"} name={"dirs"} /> {/* Add the hidden input for the selected path */}

            <div className={"mt-2"}>
                <div>
                    <input name={"date"} type={"date"} className={"p-1 mx-auto w-50 form-control button-dir"}/>
                </div>
                <select name={"number-camera"} className={"mt-2 mx-auto w-50 form-control form-control-sm p-1 bg-light border"}>
                    <option>Large select</option>
                    <option>Large select</option>
                    <option>Large select</option>
                </select>
                <select name={"number-object"} className={"mt-2 mx-auto w-50 form-control form-control-sm p-1 bg-light border"}>
                    <option>Default select</option>
                    <option>Default select</option>
                    <option>Default select</option>
                </select>
            </div>
            <div className={"row"}>
                <p className={"mt-5 w-25 mx-auto"}><input className={"btn btn-outline-secondary"} id={"btn"} type={"submit"}/></p>
            </div>
        </form>
    </div>

</div>)
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(elements);
