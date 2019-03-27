import React, {Component} from 'react';

class Users extends Component {
    constructor() {
        super();
        this.state = {
            users: [],
            submitted: false,
            response : {}
        }
        this.deleteUser = this.deleteUser.bind(this)
    }

    deleteUser(id) {
        fetch('http://localhost:8080/users/delete/'+id, {
         method: 'DELETE',
         headers: {
            'Content-Type': 'application/json'
          }
       })
       .then(response => response.json())
       .then(data => this.setState({response:data},()=>{
           alert(this.state.response.msg)
           window.location.reload()}
           ));
      }


    componentDidMount() {
        const request = new Request('http://127.0.0.1:8080/users');
        fetch(request)
            .then(response => response.json())
            .then(use => this.setState({users: use}))
            .catch(err => console.log(err));
    }

    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title">Users</h1>
                </header>

                <table className="table table-hover">
                    <thead>
                        <tr>
                            <th>Users</th>
                        </tr>
                    </thead>
                    <tbody>{
                        this.state.users !== null &&
                        
                        this
                            .state
                            .users
                            .map((item, key) => {
                                return (
                                    <tr key={key}>
                                        <td>{item.name}</td>
                                     <td>   {localStorage.getItem('usertype')==="admin" &&
                                        <button id={item.id} onClick={()=>this.deleteUser(item.id)} className="btn btn-default">Delete</button>}
                                    </td>
                                    </tr>
                                )
                            })}
                    </tbody>
                </table>
            </div>
        );
    }
}

export default Users;