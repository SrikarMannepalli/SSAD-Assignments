import React, {Component} from 'react';

class Home extends Component {
    constructor() {
        super();
        this.state = {
            scores: [],
            submitted: false,
        }
    }

    componentDidMount() {
        const request = new Request('http://127.0.0.1:8080/scoreboard');
        fetch(request)
            .then(response => response.json())
            .then(sc => this.setState({scores: sc}))
            .catch(err => console.log(err));
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title">Leaderboard</h1>
                </header>

                <table className="table table-hover">
                    <thead>
                        <tr>
                            <th>User</th>
                            <th>Score</th>
                        </tr>
                    </thead>
                    <tbody>{
                        this.state.scores !== null &&
                        this.state.scores.sort((a,b)=>{
                            return b.score-a.score ;
                        }) &&
                        this
                            .state
                            .scores
                            .map(function (item, key) {
                                return (
                                    <tr key={key}>
                                        <td>{item.name}</td>
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

export default Home;