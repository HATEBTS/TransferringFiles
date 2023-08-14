import React from "react";

const LoadingModal = () => {
  return (
    <div className="modal" id="myModal">
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-body">
            <div className="progress">
              <div
                className="progress-bar progress-bar-striped progress-bar-animated"
                role="progressbar"
                aria-valuenow="100"
                aria-valuemin="0"
                aria-valuemax="100"
                style={{ width: "100%" }}
              ></div>
            </div>
            <p className="mt-2">Загрузка...</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoadingModal;