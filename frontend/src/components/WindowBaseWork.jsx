import React from 'react';
import TabWindow from "./TabsWindow";
import ApiCallButton from "./handleExcelFile";
import CopyRd from "./CopyRd";

function BaseWork() {
  return (
    <div className={""}>
        <TabWindow />
        <div className={"container mx-auto"}>
            <div className={"p-5"}>
                <ApiCallButton />
            </div>
            <div className={"p-5"}>
                <CopyRd />
            </div>
        </div>
    </div>
  );
}

export default BaseWork;