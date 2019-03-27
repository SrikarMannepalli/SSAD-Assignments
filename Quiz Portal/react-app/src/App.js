import React, {Component} from 'react';
import ViewGenres from './components/ViewGenres'
import NewGenres from './components/CreateGenres'
import ViewQuizzes from './components/ViewQuizzes'
import ViewQuestions from './components/ViewQuestions'
import NewQuestion from './components/CreateQuestions'
import NewQuiz from './components/CreateQuiz';
import Register from './components/Register';
import EditGenre from './components/EditGenre';
import EditQuiz from './components/EditQuiz';
import EditQuestion from './components/EditQuestion';
import Login from './components/login';
import Logout from './components/logout';
import Leaderboard from './components/Scoreboard';
import Home from './components/Home';
import Users from './components/Users';
import AllUseQuizzes from './components/AllUseQuizzes';
import './App.css';

import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';

class App extends Component {
    render() {
        return (
            <div>
                <Router>
                    <div>
                        <nav className="navbar navbar-default">
                            <div className="container-fluid">
                                <div className="navbar-header">
                                    <Link className="navbar-brand" to={'/'}>React App</Link>
                                </div>
                                <ul className="nav navbar-nav">
                                    <li>
                                        <Link to={'/'}>Home</Link>
                                    </li>
                                    <li>
                                        <Link to={'/genres'}>Genres</Link>
                                    </li>
                                    {(localStorage.length===0) &&
                                    <li>
                                        <Link to={'/register'}>Register</Link>
                                    </li>
                                    }
                                    {(localStorage.length===0) &&
                                    <li>
                                        <Link to={'/login'}>Login</Link>
                                    </li>
                                    }
                                      {(localStorage.length!==0 || localStorage.getItem('logged')===1) &&
                                    <li>
                                        <Link to={'/users'}>Users</Link>
                                    </li>
                                    }
                                    {(localStorage.length!==0 || localStorage.getItem('logged')===1) &&
                                    <li>
                                        <Link to={'/usequizzes/'+localStorage.getItem('id')}>User Quizzes</Link>
                                    </li>
                                    }
                                    {(localStorage.length!==0 && localStorage.getItem('usertype')==="admin") &&
                                    <li>
                                        Welcome {localStorage.getItem('name')}
                                    </li>
                                    }
                                    {(localStorage.length!==0 || localStorage.getItem('logged')===1) &&
                                    <li>
                                        <Link to={'/logout'}>Logout</Link>
                                    </li>
                                    }
                                </ul>
                            </div>
                        </nav>
                        <Switch>
                            <Route exact path='/' component={Home} />
                            <Route exact path='/users' component={Users} />
                            <Route exact path='/usequizzes/:userid' component={AllUseQuizzes} />
                            <Route exact path='/register' component={Register} />
                            <Route exact path='/login' component={Login} />
                            <Route exact path='/logout' component={Logout} />
                            <Route exact path='/genres' component={ViewGenres}/>
                            <Route exact path='/newgenres' component={NewGenres}/>
                            <Route exact path='/scoreboard/:genreid' component={Leaderboard} />
                            <Route exact path='/genres/update/:genreid' component={EditGenre}/>
                            <Route exact path='/genres/:genreid' component={ViewQuizzes}/>
                            <Route exact path='/genres/update/:genreid/:quizid' component={EditQuiz}/>
                            <Route exact path='/genres/:genreid/:quizid' component={ViewQuestions}/>
                            <Route exact path='/update/:genreid/:quizid/:questionid' component={EditQuestion}/>
                            <Route exact path='/genres/createquiz/:genreid/:quizid' component={NewQuiz}/>
                            <Route
                                exact
                                path='/genres/createquestion/:genreid/:quizid'
                                component={NewQuestion}/>
                        </Switch>
                    </div>
                </Router>
            </div>

        );
    }
}

export default App;
