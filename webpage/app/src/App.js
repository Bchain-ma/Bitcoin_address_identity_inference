import logo from './logo.svg';
import './App.css';
import { TextInput, useState } from 'react'
import axios from 'axios'



function App() {

  const [result, setresult] = useState("")
  const [address, setaddress] = useState("1A5L6fddJncZ42GDjkdD9DzqWCpDSeTnLa")

  const submit = () => {
    if (address){
axios.post('/predict', address).then(response => {
      console.log("SUCCESS 1", response)
      if (response.data == 0) {
        setresult("This address is licit")
      } else if (response.data == 1){
        setresult("This address is illicit")
      }
      console.log(response.data)
    }).catch(error => {
      setresult("error 1 :", error.toString())
    })

    axios.post('http://api:5000/predict', address).then(response => {
      console.log("SUCCESS 2", response)
      if (response.data == 0) {
        setresult("This address is licit")
      } else if (response.data == 1){
        setresult("This address is illicit")
      }
      console.log(response.data)
    }).catch(error => {
      setresult("error 2 :", error.toString())
    })

    axios.post('http://0.0.0.0:5000/predict', address).then(response => {
      console.log("SUCCESS 3", response)
      if (response.data == 0) {
        setresult("This address is licit")
      } else if (response.data == 1){
        setresult("This address is illicit")
      }
      console.log(response.data)
    }).catch(error => {
      setresult("error 3 :", error.toString())
    })
  }
}
  return (
    <div className="App">
      
      <header className="App-header">
        <p className="App-Title">
          Bitcoin Address Checker
      </p> 
      <p >
          Please enter an address
      </p>   
        <input type="text" className="App-Input"  onChange={(evnt) => setaddress(evnt.target.value)}></input>
        <button className="App-Button" color='#306AAD' onClick={submit}>submit</button>
        <p
          className="App-result"
        >
          {result}
        </p>
      </header>
    </div>
  );
}

export default App;
