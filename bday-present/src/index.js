import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App/App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
//display content depending on page
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
