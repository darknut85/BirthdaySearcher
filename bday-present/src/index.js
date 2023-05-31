import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './components/App/App';
import { BrowserRouter } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
//display content depending on page
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
