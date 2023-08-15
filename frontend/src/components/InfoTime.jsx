import React, {useState} from 'react';
import {message} from "@tauri-apps/api/dialog";

const InfoTime = () => {
  const [modalOpen, setModalOpen] = useState(false);
  const [showMessage, setShowMessage] = useState(false);

  const openModal = () => {
    setModalOpen(true);
  };

  const closeModal = () => {
    setModalOpen(false);
    setShowMessage(false);
  };

  const toggleMessage = () => {
    setShowMessage(!showMessage);
  };

  return (
    <div className="app">
      <button
          className={"btn_1 btn-danger p-1 mt-2 ms-2"}
          type={"button"}
          onClick={() => {
          openModal();
          toggleMessage();
        }}
      >
        Инфо!!!
      </button>
      {modalOpen && (
        <div className="modal_message">
          <div className="modal-content-message">
            <h2 className={"text-center"}>Параметр времени съёмок!</h2>
            {showMessage && (
              <div className="message_modal text-center">
                Выставляйте этот параметр, когда выгружаете несколько актов за один день!
                  <br/>
                      Этот параметр - время окончания первой съемки!
              </div>
            )}
              <div className={"mx-auto w-50"}>
                  <p className={"mx-auto w-25"}>
                <button className="p-1 mt-2 btn btn-primary" onClick={() => {
                  closeModal();
                  setShowMessage(false);
                }}>Закрыть</button></p>
              </div>
          </div>
        </div>
      )}
    </div>
  );
};


export default InfoTime;