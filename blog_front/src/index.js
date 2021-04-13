import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Signin from './login'

// Welcome 이라는 컴퍼넌트를 구성하고 그 속성에 접근할 수 있음
function Welcome(props){
  return <h1>Hello, {props.name}</h1>;
  }

function GetAndPrintTime(props){
  return (
    <h1>It is {props.date.toLocaleTimeString()}</h1>
    );
  } 

function Test(){
  return(
    <div>
      <Welcome name ='Sara'></Welcome>
      <Welcome name = 'Kerrigun'></Welcome>
      <GetAndPrintTime date={new Date()}></GetAndPrintTime>
    </div>
  );
}

function printNameAndTime(){
    ReactDOM.render(
      <Test></Test>,
      document.getElementById('root')
    );
}

printNameAndTime()

ReactDOM.render(
  <Signin></Signin>,
  document.getElementById('app')
)

// ReactDOM.render(
//   document.getElementById('root')
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();