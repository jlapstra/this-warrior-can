import React, { Component } from "react";
import { Route, NavLink, HashRouter } from 'react-router-dom';
import ReactDOM from "react-dom";
import UserDashboard from './UserDashboard';
import CreateTimeSober from './CreateTimeSober';
import Img from 'react-image';
import './App.css'
import img from './ThisWarriorCan.png';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';


class MainApp extends Component {
  render() {
    return (
      <HashRouter>
        <div className="App">
          <Container className="headerBar">
            <Navbar expand="lg">
              <Navbar.Brand href="#/"><img className="imgTitle" src={ img }/></Navbar.Brand>
              <Navbar.Toggle aria-controls="basic-navbar-nav"/>
              <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                  <Nav.Link href="#/">Home</Nav.Link>
                  <Nav.Link href="#/dashboard">Dashboard</Nav.Link>
                  <Nav.Link href="#/about">About</Nav.Link>
                </Nav>
                <Nav>
                  <NavDropdown title={ this.props.data.username } id="basic-nav-dropdown">
                    <NavDropdown.Item href="#account">My Account</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="account/logout">Logout</NavDropdown.Item>
                  </NavDropdown>
                </Nav>
              </Navbar.Collapse>
            </Navbar>
          </Container>
          <div className="routeContent">
            <Route exact path="/" component={UserDashboard}/>
            <Route path="/dashboard" component={UserDashboard}/>
            <Route path="/about" component={UserDashboard}/>
            <Route path="/timesober" component={CreateTimeSober}/>
          </div>
        </div>
      </HashRouter>
    );
  }
};

export default MainApp;
