import React, { Component } from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';
import Cookies from 'js-cookie';


class ConfirmationModal extends Component {

  handleSubmit = (id, e) => {
    e.preventDefault();
    const url = '/api/deletetimesober/'.concat(id.toString()).concat("/");
    var csrftoken = Cookies.get('csrftoken');
    const conf = {
      method: "delete",
      headers: new Headers({"X-CSRFToken": csrftoken})
    };
    fetch(url, conf).then( () => {
      this.props.handleClose();
      this.props.handleHide();
    });
  };

  render() {
    return (
      <>
        <Modal.Header>
          Deletion Confirmation
        </Modal.Header>
        <Modal.Body>
          <p>Are you sure you would like to permanentley delete the habit {this.props.title}?</p>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={this.props.handleClose}>Cancel</Button>
          <Button variant="primary" onClick={(e) => this.handleSubmit(this.props.id, e)}>
            Delete {this.props.title}
          </Button>
        </Modal.Footer>
      </>
    )
  }
};

export default ConfirmationModal;
