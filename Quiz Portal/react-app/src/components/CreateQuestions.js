import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';

class NewQuestion extends Component {
    constructor(props) {
        super(props);
        this.state = {
            formData: {
                single: "",
                question: "",
                optiona: "",
                optionb: "",
                optionc: "",
                optiond: "",
                answera: false,
                answerb: false,
                answerc: false,
                answerd: false,
                img : "",
                aud : "",
                url : ""
            },
            submitted: false,
            response : {},
            quizid: props.match.params.quizid,
            genreid: props.match.params.genreid
        }

        this.handleSubmit = this
            .handleSubmit
            .bind(this);
        this.clearForm = this
            .clearForm
            .bind(this);
        this.handleSend = this
            .handleSend
            .bind(this);
    }

    clearForm = () => {
        document
            .getElementById("myForm")
            .reset();
    }

    handleSubmit(event) {
        event.preventDefault();
        var arr = [];
        var flag =0 ;
        var imgIsPresent;
        var audIsPresent;
        var count =0;
        document
            .querySelectorAll(".form-control")
            .forEach(ele => {
                if (ele.type === "text") {
                    arr.push(ele.value);
                } else if (ele.type === "checkbox") {
                    arr.push(ele.checked);
                }
                else if (ele.type === "radio") {
                    if(ele.checked) {
                        if(count===0){
                        imgIsPresent = "img"
                        }
                        else audIsPresent = "aud"
                    }
                    else {
                        if(count===0){
                        imgIsPresent = "no"
                        }
                        else {
                            audIsPresent = "no"
                        }
                    }
                    count+=1;
                }
            })
            
        this.setState({
            formData: {
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
            for (const [key, value] of Object.entries(this.state.formData)) {
                if(key !== "url" && value === "") {
                  flag = 1;
                }
              }
              if(flag === 1) {
                  alert("Fill all details")
              }
              else {
            this.clearForm();
            this.handleSend();
              }
        })
    }

    handleSend() {
        fetch('http://127.0.0.1:8080/genres/create/' + this.state.genreid + '/' + this.state.quizid, {
            method: 'POST',
            body: JSON.stringify(this.state.formData)
        }).then(response => response.json())
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
                            <input type="text" className="form-control"/>
                            <label>img</label>
                            <input type="radio" value="img" className="form-control" name="typ"/>
                            <label>aud</label>
                            <input type="radio" value="aud" className="form-control" name="typ"/>     
                            <label>Question</label>
                            <input type="text" className="form-control"/>
                            <label>Option A</label>
                            <input type="text" className="form-control"/>
                            <label>Option B</label>
                            <input type="text" className="form-control"/>
                            <label>Option C</label>
                            <input type="text" className="form-control"/>
                            <label>Option D</label>
                            <input type="text" className="form-control"/>
                            <label>Answer A</label>
                            <input type="checkbox" className="form-control"/>
                            <label>Answer B</label>
                            <input type="checkbox" className="form-control"/>
                            <label>Answer C</label>
                            <input type="checkbox" className="form-control"/>
                            <label>Answer D</label>
                            <input type="checkbox" className="form-control"/>
                            <label>Img Url</label>
                            <input type="text" className="form-control"  />
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

export default NewQuestion;