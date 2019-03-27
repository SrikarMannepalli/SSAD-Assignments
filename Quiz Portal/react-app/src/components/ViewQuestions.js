import React, {Component} from 'react';

import {Link, Redirect} from 'react-router-dom';
import './ViewQuestions.css';

class ViewQuestions extends Component {
    constructor(props) {
        super(props);
        this.state = {
            iter: 0,
            genres: [],
            genreid: parseInt(props.match.params.genreid, 10),
            quizid: parseInt(props.match.params.quizid, 10),
            outputArr: [],
            score: 0,
            submitted: false,
            delesub: false,
            response : {}
        }

        this.printQid = this
            .printQid
            .bind(this);
        this.printQuestion = this
            .printQuestion
            .bind(this);
        this.printOptiona = this
            .printOptiona
            .bind(this);
        this.printOptionb = this
            .printOptionb
            .bind(this);
        this.printOptionc = this
            .printOptionc
            .bind(this);
        this.printOptiond = this
            .printOptiond
            .bind(this);
        this.handleNext = this
            .handleNext
            .bind(this);
        this.handleSubmit = this
            .handleSubmit
            .bind(this);
        this.clearForm = this
            .clearForm
            .bind(this);
        this.deleteQuiz = this
            .deleteQuiz
            .bind(this);
    }

    clearForm = () => {
        document
            .getElementById("myForm")
            .reset();
    }

    handleSubmit(event) {
        event.preventDefault();
        this.handleNext(event);
        fetch('http://127.0.0.1:8080/finalans/'+this.state.genreid+'/'+this.state.quizid, {
            method: 'POST',
            body: JSON.stringify(this.state.outputArr)
        }).then(response => response.json()).then(data=>{
          this.setState({response:data})
          if(this.state.response.logged===0) {
            alert(this.state.response.msg)
          }
          else {
              alert("You scored "+this.state.response.score+" points")
          }
            this.setState({submitted: true})
        })
    }

    deleteQuiz(event) {
      event.preventDefault();
        var id = this.state.genres[this.state.iter].qid;
        fetch('http://localhost:8080/delete/' + this.state.genreid + '/' + this.state.quizid + '/' + id, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
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

    printQuestion() {
        var i = this.state.iter;
        if (this.state.genres === null) 
            return ""
        if (this.state.genres[i] !== undefined) {
            if (this.state.genres[i].single === "single") {
                return (this.state.genres[i].question + '...This is a single answer question')
            } else {
                return (this.state.genres[i].question + '..This is a multi question')
            }
        }
        else {
            return "abcd"
        }
    }

    printQid() {
        var i = this.state.iter;
        if (this.state.genres === null) 
            return 
        if (this.state.genres[i] !== undefined) {
            return (this.state.genres[i].qid)
        }
        else {
            return 1
        }
    }
    printOptiona() {
        var i = this.state.iter;
        if (this.state.genres === null) 
            return ""
        if (this.state.genres[i] !== undefined) {
            return (this.state.genres[i].optiona)
        }
        else {
            return "OptionA"
        }
    }
    printOptionb() {
        var i = this.state.iter;
        if (this.state.genres === null) 
            return ""
        if (this.state.genres[i] !== undefined) {
            return (this.state.genres[i].optionb)
        }
        else {
            return "OptionB"   
        }
    }
    printOptionc() {
        var i = this.state.iter;
        if (this.state.genres === null) 
            return ""
        if (this.state.genres[i] !== undefined) {
            return (this.state.genres[i].optionc)
        }
        else {
            return "OptionC"   
        }
    }
    printOptiond() {
        var i = this.state.iter;
        if (this.state.genres === null) 
            return ""
        if (this.state.genres[i] !== undefined) {
            return (this.state.genres[i].optiond)
        }
        else {
            return "OptionD"   
        }
    }

    handleNext(event) {
        event.preventDefault();
        var i = this.state.iter;
        var newf = {
            name : "guest",
            score: 0
        }
        var arr = [];

        document
            .querySelectorAll(".form-val")
            .forEach(ele => arr.push(ele.checked));

        var flag = 0;
        if (arr[0] !== this.state.genres[i].answera) {
            flag = 1;
        }
        if (arr[1] !== this.state.genres[i].answerb) {
            flag = 1;
        }
        if (arr[2] !== this.state.genres[i].answerc) {
            flag = 1;
        }
        if (arr[3] !== this.state.genres[i].answerd) {
            flag = 1;
        }
        var old_score = this.state.score;
        if(localStorage.length!==0) {
          newf.name = localStorage.getItem("name")
        }
        if (flag === 0) {
            newf.score = old_score + 1;
            this.setState({
                score: old_score + 1
            });
        } else {
            newf.score = old_score;
        }

        this
            .state
            .outputArr
            .push(newf);
        this.setState({
            iter: i + 1
        }, () => this.clearForm());
    }

    componentDidMount() {
        const request = new Request('http://localhost:8080/genres/' + this.state.genreid + '/' + this.state.quizid);
        fetch(request)
            .then(response => response.json())
            .then(gen => this.setState({genres: gen}))
            .catch(err => console.log(err));
    }

    render() {
        console.log(this.state.genres)
        if(this.state.genres !== null){
        return (
            <div className="card2">
            <div className="container2">
                <h2>Questions</h2>
                { this.state.genres[this.state.iter] !== undefined && this.state.genres[this.state.iter].img === "img" && 
            <img src={this.state.genres[this.state.iter].url} alt="img" style={{maxWidth:"600px"}} />
            }
            { this.state.genres[this.state.iter] !== undefined && this.state.genres[this.state.iter].aud === "aud" && 
                            <video src = {this.state.genres[this.state.iter].url} controls></video>
            }
                <div>
                    <h3>{this.printQuestion()}</h3>
                    <form id="myForm">
                        <div className="form-group">
                            <div>
                                <div>
                                    <label>{this.printOptiona()}</label>
                                    <input type="checkbox" className="form-val"></input>
                                    <br />
                                </div>
                                <div>
                                    <label>{this.printOptionb()}</label>
                                    <input type="checkbox" className="form-val"></input>
                                    <br />
                                </div>
                                <div>
                                    <label>{this.printOptionc()}</label>
                                    <input type="checkbox" className="form-val"></input>
                                    <br />
                                </div>
                                <div>
                                    <label>{this.printOptiond()}</label>
                                    <input type="checkbox" className="form-val"></input>
                                    <br />
                                </div>
                            </div>
                        </div>
                    </form>

                </div>
                <div><b><h3>SCORE : {this.state.score}</h3></b></div>
                {(this.state.genres !== null) && (this.state.iter < this.state.genres.length - 1) && <button onClick={this.handleNext} className="btn btn-default"><b>--></b></button>}
                {(this.state.genres !== null) && (this.state.iter >= this.state.genres.length - 1) && <button onClick={this.handleSubmit} className="btn btn-default">Submit</button>}
                {localStorage.getItem('usertype') === "admin" && <div>
                <button className="btn btn-default">
                 <Link
                        to={'/update/' + this.state.genreid + '/' + this.state.quizid + '/' + this.printQid()}> Update question</Link></button>
                    <button onClick={this.deleteQuiz} className="btn btn-default"><b>x</b></button>
                </div>
}
               
                {localStorage.getItem('usertype') === "admin" && <p>
                    <button className="btn btn-default">
                        <Link
                            to={'/genres/createquestion/' + this.state.genreid + '/' + this.state.quizid}>Add Question</Link>
                    </button>
                </p>
}
                {this.state.delesub && <div>
                    <h2>
                        Question deleted successfully.
                        <Redirect to={"/genres/"+this.state.genreid}></Redirect>
                    </h2>
                </div>
}
                {this.state.submitted && <div>
                    <h2>
                        Quiz submitted successfully.
                        <Redirect to={"/genres/"+this.state.genreid}></Redirect>
                    </h2>
                </div>
}
            </div>
            </div>
        );
    }
// else {
//     return (
//         <Redirect to={'/genres'}></Redirect>
//     )
// }
    }
}

export default ViewQuestions;