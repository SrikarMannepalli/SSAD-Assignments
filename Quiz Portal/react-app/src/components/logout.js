import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';

class Logout extends Component {
    // constructor() {
    //     super();
    //     this.state = {
    //         submitted : false,
    //         response :{}
    //     }
    //     this.handleSubmit = this.handleSubmit.bind(this);
    //     this.clearForm = this.clearForm.bind(this);
    //   }

  componentDidMount() {
      localStorage.clear();
      window.location.reload();
      alert("Logged out successfully");
  }
      
    render() {
        return (
          <Redirect to = '/genres'></Redirect>
        );
        }
    }

export default Logout;