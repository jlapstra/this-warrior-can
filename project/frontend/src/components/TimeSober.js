import React, { Component } from 'react';

import Card from 'react-bootstrap/Card';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

import Cookies from 'js-cookie';
import ConfirmationModal from './ConfirmationModal';

class TimeSober extends Component {
  constructor(props) {
    super(props);
    this.state = { 
      isHidden: false,
      show: false,
    };
  };

  handleModalShow = () => {
    this.setState({show: true});
    console.log(this.state.show);
    console.log('hi');
  };

  handleModalClose = () => {
    this.setState({show: false});
  }

  handleDelete = (id, e) => {
    e.preventDefault();
    this.handleModalShow();
  };

  handleClose = () => {
    this.setState({ isHidden: true })
  }

  render() {
    if (this.state.isHidden === true) { return false;}
    return (
      <>
        <Modal show={this.state.show} onHide={this.handleModalClose}>
          <ConfirmationModal
            title={this.props.data.title}
            id={this.props.data.id}
            handleClose={this.handleModalClose.bind(this)}
            handleHide={this.handleClose.bind(this)}
          />
        </Modal>
        <Card id="timeSober">
          <Card.Header>Stop { this.props.data.title }</Card.Header>
          <Card.Body>
            <Card.Text>
              { this.props.data.time_sober } Days {this.props.data.title} Free
            </Card.Text>
            <ButtonGroup>
              <Button variant="secondary" onClick={(e) => this.handleDelete(this.props.data.id, e)}><i className="fas fa-trash-alt"></i></Button>
            </ButtonGroup>
          </Card.Body>
        </Card>
      </>
    );
  }
}

export default TimeSober;
