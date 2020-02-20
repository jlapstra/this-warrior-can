import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';

import TimeSober from './TimeSober';
import AboutTimeSober from './AboutTimeSober';


class SoberCard extends Component {
  render() {
    if (Object.keys(this.props.data).length == 0) {
      return <AboutTimeSober />;
    }
    var timeSoberList = this.props.data.map(function(data, i) {
      return <TimeSober key={ i } data={ data } />;
    });
    return <div>{ timeSoberList }</div>;
  }
}

export default SoberCard;
