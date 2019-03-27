import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import './ViewGenres.css';

class ViewGenres extends Component {
    constructor() {
        super();
        this.state = {
            genres: [],
            response : {},
        }
        this.deleteGenre = this
            .deleteGenre
            .bind(this);
    }

    componentDidMount() {
        const request = new Request('http://127.0.0.1:8080/getgenres');
        fetch(request)
            .then(response => response.json())
            .then(gen => this.setState({genres: gen}))
            .catch(err => console.log(err));
    }

    deleteGenre(id) {
            fetch('http://localhost:8080/delete/' + id, {
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

    render() {
        return (
            <div>
                <header>
                    <h1>View All genres</h1>
                </header>
                <h3>Genre</h3>
                {(this.state.genres !== null) && this.state.genres.map((item, key) => {
                    return (
                        <div className="card">
                            <div className="container">
                                <h4>
                                    <b>
                                        <Link to={'/genres/' + item.id}>{item.genres}</Link>
                                    </b>
                                </h4>
                                {localStorage.getItem('usertype') === "admin" && 
                                <div>
                                    <button className="btn btn-default">
                                        <Link to={'/genres/update/' + item.id}>Update genre</Link>
                                    </button>
                                    <button onClick={()=>this.deleteGenre(item.id)} className="btn btn-default">
                                        <b>x</b>
                                    </button>
                                </div>
}
                                {localStorage.getItem('usertype') === "admin" && <div>
                                    <Link to='/newgenres'>
                                        <h1>
                                            <b>+</b>
                                        </h1>
                                    </Link>
                                </div>
}
                                <Link to={'/scoreboard/' + item.id}>Leaderboard</Link>
                                <br></br>
                                <b>--------------------------------------------------------------------------------------------------------------------------------------------</b>
                            </div>

                        </div>
                    )
                })}
                {
                    this.state.genres === null && localStorage.getItem('usertype') === "admin"
                     && <div>
                                    <Link to='/newgenres'>
                                        <h1>
                                            <b>+</b>
                                        </h1>
                                    </Link>
                                </div>
}
            </div>
        );
    }

}

export default ViewGenres;