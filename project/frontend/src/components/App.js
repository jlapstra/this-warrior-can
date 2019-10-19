import React, { Component } from "react";
import { Route, NavLink, HashRouter } from 'react-router-dom';
import ReactDOM from "react-dom";
import UserDashboard from './UserDashboard';
import Img from 'react-image';
import './App.css'
import img from './ThisWarriorCan.png';
import MainApp from './MainApp';
import DataProvider from './DataProvider';


const App = () => {
  return (
    <DataProvider endpoint="api/dashboard"
      render = { data => <MainApp data={ data }/>}/>
  );
};


const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
