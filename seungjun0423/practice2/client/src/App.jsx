import React, { useState } from 'react';

const App = () => {
  const [response, setResponse] = useState('');

  const sendRequest = () => {
    fetch('http://localhost:3000/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: 'Hello from React' }),
    })
      .then(res => res.json())
      .then(data => {
        setResponse(data.response);
      })
      .catch(err => {
        console.error(err);
      });
  };

  return (
    <div>
      <button onClick={sendRequest}>Send Request</button>
      <p>Server Response: {response}</p>
    </div>
  );
};

export default App;