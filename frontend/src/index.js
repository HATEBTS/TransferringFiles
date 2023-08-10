import React from 'react';
import ReactDOM from 'react-dom/client';
import './style/index.css';
import './style/bootstrap.css';
import DirectorySelectDialog from "./components/FileDialogButton";
import handleFormSubmit from "./components/handleFormSubmit";
import handleLoadExcel from "./components/handleExcelFile";
import ApiCallButton from "./components/handleExcelFile";
import LoadingModal from "./components/ModalLoading";
import CheckBox from "./components/StateUseCheckbox";


const handleDirectorySelect = (selectedPath) => {
  console.log('Selected directory path:', selectedPath);
  const selectedPathInput = document.getElementById('selectedPath');
    selectedPathInput.value = selectedPath;
  // Do whatever you want to do with the selected path here
};

const elements = (<div className="name">
    <div className={"container center-block"}>
        <form id={"form"} method={"post"} action={"#"} onSubmit={handleFormSubmit} target={"_blank"}>

                <DirectorySelectDialog onSelect={handleDirectorySelect} />
                <input type={"hidden"} id={"selectedPath"} name={"dirs"} /> {/* Add the hidden input for the selected path */}

            <div className={"mt-2"}>
                <div>
                    <input name={"date"} type={"date"} className={"p-1 mx-auto w-50 form-control button-dir"}/>
                </div>
                <select name={"number-camera"} className={"mt-2 mx-auto w-50 form-control form-control-sm p-1 bg-light border"}>

                    <option>Звено 1</option>
                    <option>Звено 2</option>
                    <option>Звено 3</option>
                    <option>Звено 4</option>
                    <option>Звено 5</option>
                    <option>Звено 6</option>
                    <option>Звено 7</option>
                    <option>Звено 8</option>
                    <option>Звено 9</option>
                    <option>Звено 10</option>

                </select>
                <input name={"number-object"} type={"text"} className={"p-1 mt-2 mx-auto w-50 form-control"} aria-label={"Small"} aria-describedby={"inputGroup-sizing-sm"}/>
            </div>
            <div className={"input-group mb-3 "}>
                <CheckBox />
            </div>
            <div className={"row"}>
                <p className={"mt-5 w-25 mx-auto"}><input className={"btn btn-outline-secondary"} id={"btn"} type={"submit"}/></p>
                <LoadingModal />
            </div>
        </form>
        <div>
            <ApiCallButton />
        </div>
    </div>
</div>)
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(elements);
