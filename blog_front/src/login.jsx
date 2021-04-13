import React from "react"
import {Component, Fragment} from 'react'

class Signin extends React.Component {

    constructor(props){
        super(props);
        this.handleIDChange = this.handleIDChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.state = {
            identifier : '',
            password : ''
        };
    }

    signInOperation(){
        console.log(this.state.identifier +'/'+ this.state.password);
        var url = 'http://localhost:8000/accounts/test/';
        const id_django = this.state.identifier;
        const password_django = this.state.password;
        var data = {'ID' : id_django, 'password' : password_django};
        fetch(url, {
            method : 'GET',
            body : JSON.stringify(data),
            credentials : 'same-origin',
            headers : {
                'Content-Type' : 'application/json'
            }
        })
        .then((response) => response.json())
        .then((json) =>{
            var tag = document.getElementById('testTag');
            tag.innerHTML += JSON.stringify(json);
        })
        .catch(error => console.log("error : ", error))
    }

    handleIDChange(e){
        this.setState({identifier: e.target.value})
    }

    handlePasswordChange(e){
        this.setState({password: e.target.value})
    }

    render(){
        return (
            <Fragment>
                <form>
                    <label for='identifier'>ID</label>
                    <input id='identifier' placeholder='ID' onChange={this.handleIDChange}></input>
                    <label for='passwd'>Password</label>
                    <input type="password" id='passwd' placeholder='password' onChange={this.handlePasswordChange}></input>
                    <button onClick={this.signInOperation}>Sign in</button>
                </form>
                <h2 id ='testTag'></h2>
            </Fragment>
        )
    }
}

class Signup extends React.Component{
    render(){
        return (
            <Fragment>
                <form>
                    <label>ID</label>
                    <input id='signUpID'></input>
                    <label>Password</label>
                    <input id='signUpPassword' type='password'></input>
                    <label>Password check</label>
                    <input id='signUpPasswordCheck' type='password'></input>
                    <label>Email</label>
                    <input id='signUpEmail' type='email'></input>
                </form>
            </Fragment>
        )
    }
}

export default Signin