import React, { useState } from 'react';
import axios from 'axios';

function LoadingModal({ showModal, onClose }) {
    const [uploadProgress, setUploadProgress] = useState(0);

    const simulateUploadProgress = () => {
        const interval = setInterval(() => {
            setUploadProgress(prevProgress => {
                if (prevProgress >= 100) {
                    clearInterval(interval);
                    onClose(); // Закрыть модальное окно по завершении
                    return prevProgress;
                }
                return prevProgress + 5;
            });
        }, 500);
    };

    const handleUpload = async () => {
        showModal(); // Открыть модальное окно

        try {
            const response = await axios.post('/api/submit-form', {
                // Ваши данные для отправки на сервер
            }, {
                onUploadProgress: progressEvent => {
                    const progress = Math.round((progressEvent.loaded / progressEvent.total) * 100);
                    setUploadProgress(progress);
                }
            });

            // Обработка успешного ответа, если необходимо
        } catch (error) {
            // Обработка ошибки, если необходимо
        }
    };

    return (
        <div className={`modal ${showModal ? 'show' : ''}`} id={"myModal"} tabIndex="-1" role="dialog">
            <div className="modal-dialog" role="document">
                <div className="modal-content">
                    <div className="modal-body">
                        <div className="progress">
                            <div className="progress-bar" role="progressbar" style={{ width: `${uploadProgress}%` }} aria-valuenow={uploadProgress} aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                        <p>Loading...</p>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default LoadingModal;