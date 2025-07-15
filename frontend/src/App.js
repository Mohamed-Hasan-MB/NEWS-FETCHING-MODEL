// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import './App.css';
import React, { useState } from 'react';

function App() {
  const [query, setQuery] = useState('');
  const [newsList, setNewsList] = useState([]);

  async function fetchNews() {
    const response = await fetch('http://localhost:5000/fetch-news', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });

    const data = await response.json();
    setNewsList(data.articles || []);
  }

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Simple News App</h1>

      <input
        type="text"
        placeholder="Enter topic..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ padding: '10px', width: '300px' }}
      />

      <button onClick={fetchNews} style={{ padding: '10px', marginLeft: '10px' }}>
        Fetch News
      </button>

      <div style={{ marginTop: '20px' }}>
        {newsList.map((news, i) => (
          <div key={i} style={{ marginBottom: '20px', borderBottom: '1px solid #ccc' }}>
            <h3>{news.title}</h3>
            <p>{news.summary || news.description}</p>
            <a href={news.url} target="_blank" rel="noopener noreferrer">Read more</a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
