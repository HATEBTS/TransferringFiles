import TabWindow from "./TabsWindow";
import HandleFormSubmit from "./handleFormSubmit";
import DirectorySelectDialog from "./FileDialogButton";
import CheckBox from "./StateUseCheckbox";
import LoadingModal from "./ModalLoading";
import React, {useState} from "react";
<<<<<<< HEAD
import ElementsTechnique from "./ElementsTechnique";
import InfoTime from "./InfoTime";
=======

const handleDirectorySelect = (selectedPath) => {
  console.log('Selected directory path:', selectedPath);
  const selectedPathInput = document.getElementById('selectedPath');
    selectedPathInput.value = selectedPath;
  // Do whatever you want to do with the selected path here
};
>>>>>>> d98c2561c024c43ff04aceff0d78677d435b3719


const HomePages = (event) => {
    const [isLoading, setIsLoading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);

    try {
      const progressCallback = (progressEvent) => {
        const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
        setUploadProgress(percentCompleted);
      };

      await HandleFormSubmit(event, progressCallback);
      alert("Готово!");
    } catch (error) {
      console.error('Error while sending form:', error);
      // Handle errors here if needed
      alert("Произошла ошибка при отправке формы.");
    } finally {
      setIsLoading(false);
      setUploadProgress(0);
    }
  };

  const handleDirectorySelect = (selectedPath) => {
    console.log('Selected directory path:', selectedPath);
    const selectedPathInput = document.getElementById('selectedPath');
    selectedPathInput.value = selectedPath;
  };
    return (
        <div className="name">
            <TabWindow />
            <div className={"container center-block"}>
                <form id={"form"} method={"post"} action={"#"} onSubmit={HandleFormSubmit} target={"_blank"}>
                        <DirectorySelectDialog onSelect={handleDirectorySelect} />
                        <input type={"hidden"} id={"selectedPath"} name={"dirs"} /> {/* Add the hidden input for the selected path */}

                    <div className={"mt-2"}>
                        <div>
                            <input name={"date"} type={"date"} className={"transparent-input p-1 mx-auto w-50 form-control button-dir transparent-input"}/>
                        </div>
                        <ElementsTechnique />

                        <input name={"number-object"} type={"text"} placeholder={"Введите номер акта"} className={"p-1 mt-2 mx-auto w-50 form-control transparent-input"} aria-label={"Small"} aria-describedby={"inputGroup-sizing-sm"}/>
                    </div>
                    <div className={"justify-content-between"}>
                        <div className={"input-group mb-3"}>
                            <CheckBox />

<<<<<<< HEAD
                        </div>
                    </div>
=======
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
>>>>>>> d98c2561c024c43ff04aceff0d78677d435b3719

                    <div className={"row"}>
                        <p className={"mt-5 w-25 mx-auto"}><input className={"btn btn-outline-secondary"} id={"btn"} type={"submit"}/></p>
                        <LoadingModal />
                    </div>
                </form>


            </div>

        </div>
    )

}

export default HomePages;