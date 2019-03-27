import React, {Component} from 'react';
import {Link, Redirect} from 'react-router-dom';

class ViewQuizzes extends Component {
    constructor(props) {
        super(props);
        this.state = {
            genres: [],
            genreid: parseInt(props.match.params.genreid, 10),
            response:{}
        }
        this.findMax = this
            .findMax
            .bind(this)
        this.deleteQuiz = this
            .deleteQuiz
            .bind(this)
    }

    deleteQuiz(id) {
        fetch('http://localhost:8080/delete/' + this.state.genreid + '/' + id, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(response => response.json())
        .then(data => this.setState({response:data},()=>alert(this.state.response.msg)));
        window
            .location
            .reload();
    }

    findMax() {
        var max = 0;
        if (this.state.genres == null) 
            return 1;
        this
            .state
            .genres
            .forEach((item) => {
                if (item.id > max) {
                    max = item.id
                }
            })
        max = max + 1;
        return max
    }

    componentDidMount() {
        const request = new Request('http://127.0.0.1:8080/genres/' + this.state.genreid);
        fetch(request)
            .then(response => response.json())
            .then(gen => this.setState({genres: gen}))
            .catch(err => console.log(err));
    }

    render() {
        return (
            <div>
                <header>
                    <h1>View All quizzes</h1>
                </header>
                <h3>Quizzes</h3>
                {(this.state.genres != null) && <div>{this
                        .state
                        .genres
                        .map((item, key) => {
                            return (
                                <div className="card">
                                    <div className="container">
                                        <h4>
                                            <b>
                                                <Link to={'/genres/' + this.state.genreid + '/' + item.id}>{item.name}</Link>
                                            </b>
                                        </h4>
                                        {localStorage.getItem('usertype') === "admin" && <div>
                                            <button className="btn btn-default">
                                                <Link to={'/genres/update/' + this.state.genreid + '/' + item.id}>Update</Link>
                                            </button>
                                            <button onClick={()=>this.deleteQuiz(item.id)} className="btn btn-default">
                                                <b>x</b>
                                            </button>
                                        </div>
}
                                        {localStorage.getItem('usertype') === "admin" && <div>
                                            <h1>
                                                <b>
                                                    <Link to={'/genres/createquiz/' + this.state.genreid + '/' + this.findMax()}>+</Link>
                                                </b>
                                            </h1>
                                            <b>--------------------------------------------------------------------------------------------------------------------------------------------</b>
                                        </div>
                                        
}</div>

                                </div>
                            )
                        })}
                        
                         {this.state.submitted && <div>
                        <h2>
                            Quiz deleted successfully.
                            <Redirect to="/genres">abcd</Redirect>
                        </h2>
                    </div>
}
                </div>
}
{
    ( this.state.genres === null) && localStorage.getItem('usertype') === "admin" && 
     <h1>
                         <b>
                             <Link to={'/genres/createquiz/' + this.state.genreid + '/' + this.findMax()}>+</Link>
                         </b>
                     </h1>
 }
            </div>
        );
    }
}

export default ViewQuizzes;