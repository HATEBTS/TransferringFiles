import React from 'react';
import { Portal } from 'react-portal';

const LoadingModal = ({ isOpen, message }) => {
  if (!isOpen) {
    return null;
  }

  return (
    <Portal>
      <div className="loading-modal-overlay">
        <div className="loading-modal">
          <div className="loading-spinner"></div>
          <div className="loading-message">{message}</div>
        </div>
      </div>
    </Portal>
  );
};

export default LoadingModal;

