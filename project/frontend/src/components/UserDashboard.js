import React, { Component } from "react";
import DataProvider from './DataProvider';
import UserData from './UserData';
import TimeSober from './TimeSober';

class UserDashboard extends Component {
  render() {
    return (
      <div>
        <DataProvider endpoint="api/timesober"
          render = { data => <TimeSober data={ data }/>}/>
        <div className="thisIsYou" style={{color: '#84AABB'}}>
          <p>This is you</p>
          <span style={{color: '#D3E2E8'}}>
            <i className="fas fa-user-circle fa-10x"></i>
          </span>
          <p>And you got this</p>
        </div>
      </div>
    );
  }
}

export default UserDashboard;
