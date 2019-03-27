import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';


class NewQuiz extends Component {
  constructor(props) {
    super(props);
    this.state = {
      iter : 0,
      savequizname : "",
      outputArr : [],
      submitted: false,
      response : {},
      quizid : parseInt(props.match.params.quizid,10),
      genreid : parseInt(props.match.params.genreid,10)
    }
    this.handleNext = this.handleNext.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.clearForm = this.clearForm.bind(this);
  }

  clearForm = () => {
    document.getElementById("myForm").reset(); 
  }

  handleSubmit (event) {
    event.preventDefault();
    this.handleNext(event);
    fetch('http://127.0.0.1:8080/genres/create/'+this.state.genreid, {
     method: 'POST',
     body: JSON.stringify(this.state.outputArr)
   })
      .then(response => response.json())
      .then(data=>this.setState({response:data}))
      .then(()=>{
        alert(this.state.response.msg)
        if(this.state.response.success === true) {
          this.setState({submitted: true})
        }
        else {
          this.setState({submitted: false})
        }
      })
  }

handleNext(event) {
  event.preventDefault();
  var newf = {
    questionqid : 1,
        quizid : 1,
        quizname : "", 
        genreid: 1,
        single : "",
        question : "",
        optiona : "",
        optionb : "",
        optionc : "",
        optiond : "",
        answera : false,
        answerb : false,
        answerc : false,
        answerd : false,
        img : "",
        aud : "",
        url : ""
  }
  newf.quizid = this.state.quizid;
  newf.genreid = this.state.genreid;
  var imgIsPresent;
  var audIsPresent;
  var arr = [];
  var count = 0;
  document.querySelectorAll(".form-control").forEach(ele =>{
    if(ele.type === "text") {
      arr.push(ele.value);
    }
    else if(ele.type === "checkbox") {
      arr.push(ele.checked);
    }
    else if(ele.type === "radio") {
      if(ele.checked) {
        if(count===0){
        imgIsPresent = "img";
        }
        else audIsPresent = "aud";
      }
      else {
        if(count===0){
        imgIsPresent = "no";
        }
        else audIsPresent = "no";
      }
      count +=1;
    }
  } )
  var i = this.state.iter;
  if(i ===0){
  newf.quizname = arr[0];
  newf.single = arr[1];
  newf.question = arr[2];
  newf.optiona = arr[3];
  newf.optionb = arr[4];
  newf.optionc = arr[5];
  newf.optiond = arr[6];
  newf.answera = arr[7];
  newf.answerb = arr[8];
  newf.answerc = arr[9];
  newf.answerd = arr[10];
  newf.url = arr[11];
  newf.img = imgIsPresent;
  newf.aud = audIsPresent;
  this.setState({savequizname:arr[0],iter:i+1},()=>this.clearForm());
  }
  else
  {
    newf.quizname = this.state.savequizname;
    newf.single = arr[0];
    newf.question = arr[1];
    newf.optiona = arr[2];
    newf.optionb = arr[3];
    newf.optionc = arr[4];
    newf.optiond = arr[5];
    newf.answera = arr[6];
    newf.answerb = arr[7];
    newf.answerc = arr[8];
    newf.answerd = arr[9];
    newf.url = arr[10];
    newf.img = imgIsPresent;
    newf.aud = audIsPresent;
    this.setState({iter:i+1},()=>this.clearForm());
  }
  var flag = 0;
  for (const [key, value] of Object.entries(newf)) {
    if(key !== "url" && key!=="genre" && value === "") {
      flag = 1;
    }
  }
  if(flag===0) {
    this.state.outputArr.push(newf);
  }
  else {
    alert("Fill all details");
  }
}

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Create a New Quiz</h1>
        </header>
        <br/><br/>
        <div className="formContainer">
          <form id="myForm">
            <div className="form-group">
            <label>Quiz Name</label>
            { (this.state.iter ===0) &&
                <input type="text" className="form-control" />
            }
            {
              (this.state.iter !== 0) && 
              <p>{this.state.savequizname}</p>
            }
                <label>Question Type</label>
                <input type="text" className="form-control" />
                <label>img</label>
                <input type="radio" value="img" className="form-control" name="typ"/>
                <label>aud</label>
                <input type="radio" value="aud" className="form-control" name="typ"/>
                <label>Question</label>
                <input type="text" className="form-control"  />
                <label>Option A</label>
                <input type="text" className="form-control"  />
                <label>Option B</label>
                <input type="text" className="form-control"  />
                <label>Option C</label>
                <input type="text" className="form-control"  />
                <label>Option D</label>
                <input type="text" className="form-control"  />
                <label>Answer A</label>
                <input type="checkbox" className="form-control" />
                <label>Answer B</label>
                <input type="checkbox" className="form-control" />
                <label>Answer C</label>
                <input type="checkbox" className="form-control" />
                <label>Answer D</label>
                <input type="checkbox" className="form-control"  />
                <label>Url</label>
                <input type="text" className="form-control"  />
            </div>
                <button onClick={this.handleNext} className="btn btn-default">Next</button>
                <button onClick={this.handleSubmit} className="btn btn-default">Submit</button>
          </form>
        </div>

        {this.state.submitted &&
          <div>
            <h2>
              New Quiz added successfully.
              <Redirect to={'/genres/'+this.state.genreid}></Redirect>
            </h2>
          </div>
        }
      </div>
    );
  }
}

export default NewQuiz;