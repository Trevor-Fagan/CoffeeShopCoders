import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://coffeeshopcoders.com/api')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching data: ', error);
      });
  }, []);

  return (
    <div className="App">
      <div className="main-header">
        <h1>Coffee Shop Coders</h1>
      </div>

      <div className="main-content">
        Backend content: {data}
      </div>

      <div className="footer">
        <p>© CoffeeShopCoders, 2023</p>
      </div>
    </div>
  );
}

export default App;
