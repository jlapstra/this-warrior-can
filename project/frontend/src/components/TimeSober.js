import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';


class TimeSober extends Component {
  render() {
    return (
      <Card id="timeSober">
        <Card.Header>Stop { this.props.data.title }</Card.Header>
        <Card.Body>
          <Card.Text>
            { this.props.data.time_sober } Days {this.props.data.title} Free
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default TimeSober;
