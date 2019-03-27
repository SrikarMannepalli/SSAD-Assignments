import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';

class Login extends Component {
    constructor() {
        super();
        this.state = {
            submitted : false,
            response :{}
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
          } )
          newf.username = arr[0];
          newf.password = arr[1];
        //   this.clearForm();
        fetch('http://127.0.0.1:8080/login', {
         method: 'POST',
         body: JSON.stringify(newf)
       })
       .then(response => response.json()).then(data=>{
        this.setState({response:data})
        if(this.state.response.logged===1) {
            localStorage.setItem('usertype',this.state.response.user)
            localStorage.setItem('logged',1)
            localStorage.setItem('name',this.state.response.name)
            localStorage.setItem('id',this.state.response.id)
          this.setState({submitted: true})
        }
      }).then(()=>{
          alert(this.state.response.msg)
          window.location.reload()
      })
  }
      
    render() {
        return (
          <div className="card1">
            <br/><br/>
            <div className="container1">
              <form id="myForm">
                <div className="form-group">
                    <label>Username</label>
                    <input type="text" className="form-control" />
                    <label>Password</label>
                    <input type="password" className="form-control"  />
                </div>
                    <button onClick={this.handleSubmit} className="btn btn-default">Submit</button>
              </form>
            </div>
            {
                this.state.submitted === true &&
                <Redirect to="/genres"></Redirect> 
            }
          </div>
        );
        }
    }

export default Login;