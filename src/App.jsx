import { useState, useEffect } from 'react';

function App() {
  const [stocks, setStocks] = useState([]);

  useEffect(() => {
    
    fetch('http://127.0.0.1:8000/api/stocks')
      .then((response) => response.json())
      .then((data) => setStocks(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <div style={{ padding: '40px', fontFamily: 'system-ui, sans-serif' }}>
      <h1 style={{ color: '#2c3e50' }}>Live EGX Stock Monitor</h1>
      
      <table style={{ width: '100%', maxWidth: '600px', borderCollapse: 'collapse', marginTop: '20px' }}>
        <thead>
          <tr style={{ backgroundColor: '#f8f9fa', borderBottom: '2px solid #dee2e6', textAlign: 'left' }}>
            <th style={{ padding: '12px' }}>Ticker String</th>
            <th style={{ padding: '12px' }}>Last Price (EGP)</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map((stock) => (
            <tr key={stock.ticker} style={{ borderBottom: '1px solid #dee2e6' }}>
              <td style={{ padding: '12px', fontWeight: 'bold' }}>{stock.ticker}</td>
              <td style={{ padding: '12px', color: '#2ecc71', fontWeight: 'bold' }}>{stock.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;