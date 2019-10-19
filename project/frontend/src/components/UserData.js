import React, { Component } from 'react';


class UserData extends Component {
  render() {
    return (

      <h1>{ this.props.data.username }</h1>


    );
  }

}

export default UserData;
