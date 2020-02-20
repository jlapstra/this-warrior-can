import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';


class AboutTimeSober extends Component {
  render() {
    return (
      <Card id="timeSober">
        <Card.Header>Habit Breaker</Card.Header>
        <Card.Body>
          <Card.Title>Have a habit you hope to stop?</Card.Title>
          <Card.Text>
            Create a habit and start your streak! Once created, you will be able to reset and see results of previous streaks.
          </Card.Text>
          <Button>Track my Habit</Button>
        </Card.Body>
      </Card>
    );
  }
}

export default AboutTimeSober;
