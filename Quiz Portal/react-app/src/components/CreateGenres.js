import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';
// import './NewGenre.css';

class NewGenres extends Component {
  constructor() {
    super();
    this.state = {
      formData: {
        genres: "",
        response : {}
      },
      submitted: false,
    }
    this.handleGenreChange = this.handleGenreChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit (event) {
    event.preventDefault();
    if(this.state.genres === "") {
      alert("Fill the name");
    }
    else {
    fetch('http://127.0.0.1:8080/creategenres', {
     method: 'POST',
     body: JSON.stringify(this.state.formData)
   })
      .then(response => response.json())
      .then(data=>{this.setState({response:data})})
      .then(()=>{
        if(this.state.response.success === true){
          alert(this.state.response.msg);
          this.setState({submitted:true});
        }
        else {
          alert(this.state.response.msg);
          this.setState({submitted:false});
        }
      }
      );
  }
}

  handleGenreChange(event) {
      this.setState({formData:{genres:event.target.value} })
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
                <label>Genre Name</label>
                <input type="text" className="form-control" value={this.state.genres} onChange={this.handleGenreChange}/>
            </div>
                <button type="submit" className="btn btn-default">Submit</button>
          </form>
        </div>

        {this.state.submitted &&
          <div>
            <h2>
              New genre added successfully.
              <Redirect to="/genres"></Redirect>
            </h2>
          </div>
        }

      </div>
    );
  }
}

export default NewGenres;