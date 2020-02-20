import React, { Component } from 'react';
import CardColumns from 'react-bootstrap/CardColumns';

import TimeSober from './TimeSober';
import AboutTimeSober from './AboutTimeSober';


class SoberCard extends Component {
  render() {
    if (Object.keys(this.props.data).length == 0) {
      return <AboutTimeSober key="no data" />;
    }
    var timeSoberList = this.props.data.map(function(data, i) {
      return <TimeSober key={ i } data={ data } />;
    });
    timeSoberList.push(<AboutTimeSober key="data" />);
    return <div>{ timeSoberList }</div>;
  }
}

export default SoberCard;
