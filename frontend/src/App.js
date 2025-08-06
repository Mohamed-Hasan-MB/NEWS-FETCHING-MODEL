import './App.css';
import React, { useState } from 'react';

function App() {
  const [query, setQuery] = useState('');
  const [newsList, setNewsList] = useState([]);

  async function fetchNews() {
    
    const response = await fetch('http://localhost:5000/summarize', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ topic: query }),  // key must match "topic" in backend
    });
    const data = await response.json();
    setNewsList(data.articles || []);
  }

  return (
    <div className="container">
      <h1>Simple News App</h1>

      <div className="input-group">
        <input
          type="text"
          placeholder="Enter topic..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={fetchNews}>Fetch News</button>
      </div>

      <div style={{ marginTop: '30px' }}>
        {newsList.map((news, i) => (
          <div key={i} className="news-item">
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
