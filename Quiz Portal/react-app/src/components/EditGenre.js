import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';

class EditGenre extends Component {
  constructor(props) {
    super(props);
    this.state = {
        formData: {
            genreid: props.match.params.genreid,
            genrename: ""
        },
        response : {},
      submitted: false,
      genreid: props.match.params.genreid
    }
    this.handleGenreChange = this.handleGenreChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit (event) {
    event.preventDefault();
    fetch('http://127.0.0.1:8080/genres/update/'+this.state.genreid, {
     method: 'PUT',
     body: JSON.stringify(this.state.formData),
     headers: {
        'Content-Type': 'application/json'
      }
   })
      .then(response => response.json())
      .then(data =>this.setState({response:data}))
      .then(()=>{
        alert(this.state.response.msg)
        if(this.state.response.success === true){
          this.setState({submitted: true})
        }
        else {
          this.setState({submitted: false})
        }
      })
  }

  handleGenreChange(event) {
      this.setState({formData:{genreid:this.state.genreid,genrename:event.target.value}})
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Create a New Genre</h1>
        </header>
        <br/><br/>
        <div className="formContainer">
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
                <label>New Genre Name</label>
                <input type="text" className="form-control" onChange={this.handleGenreChange}/>
            </div>
                <button type="submit" className="btn btn-default">Submit</button>
          </form>
        </div>

        {this.state.submitted &&
          <div>
            <h2>
              Genre name modified successfully.
              <Redirect to="/genres"></Redirect>
            </h2>
          </div>
        }
      </div>
    );
  }
}

export default EditGenre;