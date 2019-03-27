import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';
import './Register.css';

class Register extends Component {
    constructor(props) {
        super(props);
        this.state = {
            submitted : false,
        response : {},
        }
        this.handleSubmit = this.handleSubmit.bind(this);
        this.clearForm = this.clearForm.bind(this);
      }
      
      clearForm = () => {
        document.getElementById("myForm").reset(); 
      }

      handleSubmit (event) {
        event.preventDefault();
        var newf = {
            id : 1,
            type : "",
            username : "",
            password : " "
        };
        var arr=[];
        document.querySelectorAll(".form-control").forEach(ele =>{
            if(ele.type === "text") {
              arr.push(ele.value);
            }
            else if(ele.type === "password") {
              arr.push(ele.value);
            }
            else if(ele.type === "radio") {
                if(ele.checked) {
                    arr.push(ele.value);
                }
            }
          } )
          newf.id = 1;
          newf.type = arr[2];
          newf.username = arr[0];
          newf.password = arr[1];
        fetch('http://127.0.0.1:8080/signup', {
         method: 'POST',
         body: JSON.stringify(newf)
       })
          .then(response => response.json()).then(data=>{
            this.setState({response:data})
            if(this.state.response.logged===1) {
              this.setState({submitted: true})
            }
            alert(this.state.response.msg)
          })
      }
      


    render() {
        return (
          <div className="card1">
            <div className="container1">
              <form id="myForm">
                <div className="form-group">
                    <label>Username</label>
                    <input type="text" className="form-control" />
                    <label>Password</label>
                    <input type="password" className="form-control"  />
                    <p>Usertype</p>
                    <label>Admin</label>
                    <input type="radio" value="admin" className="form-control" name="usertype"></input>
                    <label>User</label>
                    <input type="radio" value="user" className="form-control" name="usertype"></input>
                </div>
                    <button onClick={this.handleSubmit} className="btn btn-default">Submit</button>
              </form>
            </div>
    
            {this.state.submitted &&
              <div>
                <h2>
                  New User added successfully.
                </h2>
                <Redirect to="/login"></Redirect>
              </div>
            }
          </div>
        );
        }
    }

export default Register;