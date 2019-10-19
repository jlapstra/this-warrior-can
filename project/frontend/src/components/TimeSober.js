import React, { Component } from 'react';


class TimeSober extends Component {
  render() {
    return (
      <div>
        <h1>{this.props.data.title} Free </h1>
        <h2>{this.props.data.time_sober} Days</h2>
      </div>
    );
  }
}

export default TimeSober;
