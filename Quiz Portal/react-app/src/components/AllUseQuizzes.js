import React, {Component} from 'react';

class Leaderboard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            scores: [],
            submitted: false,
            userid : parseInt(props.match.params.userid,10)
        }
    }

    componentDidMount() {
        const request = new Request('http://127.0.0.1:8080/usequizzes/' + this.state.userid);
        fetch(request)
            .then(response => response.json())
            .then(sc => this.setState({scores: sc}))
            .catch(err => console.log(err));
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title">User Quizzes</h1>
                </header>

                <table className="table table-hover">
                    <thead>
                        <tr>
                            <th>User</th>
                            <th>Quiz</th>
                            <th>Score</th>
                        </tr>
                    </thead>
                    <tbody>{
                        this.state.scores !== null &&
                        this
                            .state
                            .scores
                            .map(function (item, key) {
                                return (
                                    <tr key={key}>
                                    {console.log(item)}
                                        <td>{item.name}</td>
                                        <td>{item.quiz}</td>
                                        <td>{item.score}</td>
                                    </tr>
                                )
                            })}
                    </tbody>
                </table>
            </div>
        );
    }
}

export default Leaderboard;