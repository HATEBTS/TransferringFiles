import React from 'react';
import TabWindow from "./TabsWindow";
import ApiCallButton from "./handleExcelFile";

function BaseWork() {
  return (
    <div className={""}>
        <TabWindow />

        <div className={"p-5 container"}>
            <ApiCallButton />
        </div>
    </div>
  );
}

export default BaseWork;