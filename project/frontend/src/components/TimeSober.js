import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';


class TimeSober extends Component {
  render() {
    return (
      <Card className="timeSober">
        <Card.Header>Habbit Breaker</Card.Header>
        <Card.Body>
          <Card.Title>{ this.props.data.title } Free</Card.Title>
          <Card.Text>
            { this.props.data.time_sober } Days
          </Card.Text>
        </Card.Body>
      </Card>
    );
  }
}

export default TimeSober;
