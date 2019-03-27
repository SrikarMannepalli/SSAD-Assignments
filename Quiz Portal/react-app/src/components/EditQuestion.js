import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';

class EditQuestion extends Component {
  constructor(props) {
    super(props);
    this.state = {
      submitted: false,
      question : {
        quizid : 1,
        questionqid : 1,
        genreid : 1,
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
      },
      response : {},
      genreid: parseInt(props.match.params.genreid,10),
      quizid: parseInt(props.match.params.quizid,10),
      questionid: parseInt(props.match.params.questionid,10)
    }
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleSend = this.handleSend.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    var arr = [];
    var count = 0;
    var audIsPresent;
    var imgIsPresent;
    document
        .querySelectorAll(".form-control")
        .forEach(ele => {
            if (ele.type === "text") {
                arr.push(ele.value);
            } else if (ele.type === "checkbox") {
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
                count+=1;
              }
        })
    this.setState({
        formData: {
            quizid : this.state.quizid,
            questionqid : this.state.questionid,
            genreid : this.state.genreid,
            single: arr[0],
            question: arr[1],
            optiona: arr[2],
            optionb: arr[3],
            optionc: arr[4],
            optiond: arr[5],
            answera: arr[6],
            answerb: arr[7],
            answerc: arr[8],
            answerd: arr[9],
            img : imgIsPresent,
            aud : audIsPresent,
            url : arr[10]
        }
    }, () => {
        console.log(this.state.formData)
        var flag = 0;
        for (const [key, value] of Object.entries(this.state.formData)) {
            if(key !== "url" && value === "") {
              flag = 1;
            }
          }
          if(flag === 1) {
              alert("Fill all details")
          }
          else {
            this.handleSend();
          }
    })
}
  handleSend () {
      console.log(this.state.formData)
    fetch('http://localhost:8080/genres/update/'+this.state.genreid+'/'+this.state.quizid+'/'+this.state.questionid, {
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

  componentDidMount() {
    var count = 0;
    var cnt =0;
    const request = new Request('http://localhost:8080/getque/'+this.state.genreid+'/'+this.state.quizid+'/'+this.state.questionid);
    fetch(request)
    .then(response => response.json())
    .then(que => {
      this.setState({question: que})}).then(()=>{
        document.querySelectorAll(".form-control").forEach(ele =>{
            if(ele.type === "radio") {
                if(cnt===0){
                if(this.state.question.img === "img") {
                    ele.checked = true;
                }
                else {
                    ele.checked = false;
                }
            }
            else {
                if(this.state.question.aud === "aud") {
                    ele.checked = true;
                }
                else {
                    ele.checked = false;
                }
            }
            cnt++;
            }
          if(ele.type === "checkbox") {
                if(count===0 && this.state.question.answera===true) {
                  ele.checked  = true; 
                }
                else if(count===1 && this.state.question.answerb===true) {
                  ele.checked = true;
                }
                else if(count===2 && this.state.question.answerc===true) {
                  ele.checked = true;
                }
                else if(count===3 && this.state.question.answerd===true) {
                  ele.checked = true;
                }
                else {
                    ele.checked = false;
                }
                count+=1;
              }
            } )
      })
    .catch(err => console.log(err));
  }
   

    render() {
      return (
          <div className="App">
              <header className="App-header">
                  <h1 className="App-title">Add a Question</h1>
              </header>
              <br/><br/>
              <div className="formContainer">
                  <form id="myForm">
                      <div className="form-group">
                          <label>Question Type</label>
                          <input type="text" defaultValue = {this.state.question.single} className="form-control"/>
                          <label>img</label>
                          <input type="radio" value="img" className="form-control" name="typ"/>
                          <label>aud</label>
                          <input type="radio" value="aud" className="form-control" name="typ"/>
                          <label>Question</label>
                          <input type="text" defaultValue = {this.state.question.question} className="form-control"/>
                          <label>Option A</label>
                          <input type="text" defaultValue = {this.state.question.optiona} className="form-control"/>
                          <label>Option B</label>
                          <input type="text" defaultValue = {this.state.question.optionb} className="form-control"/>
                          <label>Option C</label>
                          <input type="text" defaultValue = {this.state.question.optionc} className="form-control"/>
                          <label>Option D</label>
                          <input type="text" defaultValue = {this.state.question.optiond} className="form-control"/>
                          <label>Answer A</label>
                          <input type="checkbox"  className="form-control"/>
                          <label>Answer B</label>
                          <input type="checkbox"  className="form-control"/>
                          <label>Answer C</label>
                          <input type="checkbox"  className="form-control"/>
                          <label>Answer D</label>
                          <input type="checkbox"  className="form-control"/>
                          <label>Url</label>
                          <input type="text" defaultValue = {this.state.question.url} className="form-control"  />
                      </div>
                      <button onClick={this.handleSubmit} className="btn btn-default">Submit</button>
                  </form>
              </div>

              {this.state.submitted && <div>
                  <h2>
                      <Redirect to={'/genres/'+this.state.genreid+'/'+this.state.quizid}></Redirect>
                  </h2>
              </div>
}
          </div>
      );
  }
}
export default EditQuestion;