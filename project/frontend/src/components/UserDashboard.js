import React, { Component } from "react";
import DataProvider from './DataProvider';
import UserData from './UserData';
import SoberCard from './SoberCard';
import Card from 'react-bootstrap/Card';
import CardColumns from 'react-bootstrap/CardColumns';

class UserDashboard extends Component {
  render() {
    return (
      <CardColumns>
        <DataProvider endpoint="api/timesober"
          render = { data => <SoberCard data={ data }/>}/>
        <Card className="thisIsYou">
          <Card.Body>
            <Card.Text>
              This is you
              <span style={{color: '#D3E2E8'}}>
                <i className="fas fa-user-circle fa-10x"></i>
              </span>
              And you got this
            </Card.Text>
          </Card.Body>
        </Card>
      </CardColumns>
    );
  }
}

export default UserDashboard;
