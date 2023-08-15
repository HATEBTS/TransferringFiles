import React from 'react';
import TabWindow from "./TabsWindow";
import ApiCallButton from "./handleExcelFile";
import CopyRd from "./CopyRd";
import MoveAct from "./MoveAct";
import logo from "../images/logo.gif";
import SheetsG from "./SheetsG";

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
                <MoveAct />
                <SheetsG />
                <img className={"size-dance"} src={logo} alt="loading..." />
            </div>
        </div>
    </div>
  );
}

export default BaseWork;