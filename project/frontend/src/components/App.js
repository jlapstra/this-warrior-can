import React, { Component } from "react";
import { BrowseRouter as Router, Route} from 'react-router-dom';
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";

//import PrivateRoute from './PrivateRoute';
//import UserDashboard from './UserDashboard';
//import LoginForm from './LoginForm';


const App = () => (
  <DataProvider endpoint="api/lead/" 
                render={data => <Table data={data} />} />
);

//<Router>
//  <Route path="/account/login" component={LoginForm} />
//  <PrivateRoute path="/" component={UserDashboard} />
//</Router>

const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
