import React from 'react';
import { Link } from 'react-router-dom';

function TabWindow() {
    return (
    <ul className={"nav nav-tabs"}>
      <li className={"nav-item"}>
        <Link className={"nav-link"} to="/home">Главная</Link>
      </li>
      <li className={"nav-item"}>
        <Link className={"nav-link"} to="/base">Статистика</Link>
      </li>
    </ul>
  );
}

export default TabWindow;




