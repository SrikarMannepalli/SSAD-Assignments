import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';

class EditQuiz extends Component {
  constructor(props) {
    super(props);
    this.state = {
        formData: {
            quizname: ""
        },
        response : {},
      submitted: false,
      genreid: props.match.params.genreid,
      quizid: props.match.params.quizid
    }
    this.handleQuizChange = this.handleQuizChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit (event) {
    event.preventDefault();
    fetch('http://localhost:8080/genres/update/'+this.state.genreid+'/'+this.state.quizid, {
     method: 'PUT',
     body: JSON.stringify(this.state.formData),
     headers: {
        'Content-Type': 'application/json'
      }
   })
   .then(response => response.json())
   .then(data => this.setState({response:data},()=>{
    if(this.state.response.success === true) this.setState({submitted: true})
    else  this.setState({submitted: false})
    alert(this.state.response.msg);
   }))
}

  handleQuizChange(event) {
      this.setState({formData:{quizname:event.target.value}})
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Update quiz name</h1>
        </header>
        <br/><br/>
        <div className="formContainer">
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
                <label>New Quiz Name</label>
                <input type="text" className="form-control" onChange={this.handleQuizChange}/>
            </div>
                <button type="submit" className="btn btn-default">Submit</button>
          </form>
        </div>

        {this.state.submitted &&
              <Redirect to={"/genres/"+this.state.genreid}/>
        }
      </div>
    );
  }
}

export default EditQuiz;