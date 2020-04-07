import React, { useState } from 'react';
import Form from 'react-bootstrap/Form';
import FormGroup from 'react-bootstrap/FormGroup';
import Button from 'react-bootstrap/Button';
import DatePicker from 'react-date-picker';
import { useHistory } from 'react-router-dom';
import Cookies from 'js-cookie';


function CreateTimeSober(props) {
  const [date, setDate] = useState(new Date());
  const [title, setTitle] = useState('');
  let history = useHistory();

  const onDateChange = e => {
    setDate(e);
  };

  const onTitleChange = e => {
    setTitle(e.target.value);
  };

  const handleSubmit = e => {
    e.preventDefault();
    var csrftoken = Cookies.get('csrftoken');
    const form = {
      title: title,
      sober_date: date.toISOString().split('T')[0]
    };
    const conf = {
      method: "post",
      body: JSON.stringify(form),
      headers: new Headers({ "Content-Type": "application/json", "X-CSRFToken": csrftoken })
    };
    fetch('/api/timesober/', conf).then( () => {
      history.push("/dashboard");
    });
  };

  return (
    <Form>
      <Form.Group>
        <Form.Label>Title</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter Habit Name"
          onChange={ onTitleChange }
          value={ title }
        />
      </Form.Group>
      <Form.Group>
        <Form.Label>Date Started</Form.Label>
        <DatePicker
          onChange={ onDateChange }
          value={ date }
        />
      </Form.Group>
      <Form.Group>
        <Button type="submit" onClick={ handleSubmit } >Create Habbit</Button>
      </Form.Group>
    </Form>
  );
}

export default CreateTimeSober;
