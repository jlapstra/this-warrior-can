// Used to see if the user is logged in.
//
//

import React from 'react';
import { Redirect, Route } from 'react-router-dom';


const PrivateRoute = ({ component: Component, ...rest }) => {

  //auth somehow
  const isLoggedIn = 

  return (
    <Route
      {...rest}
      render={props =>
        isLoggedIn ? (
          <Component {...props} />
        ) : (
          <Redirect to={{ pathname: 'account/login', state: { from: props.location } }} />
        )
      }
    />
  )
}
