import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Home from './containers/Home';
import Error404 from './containers/errors/Error404';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="*" element={<Error404 />} />
        <Route exact path='/' element={<Home />} />
      </Routes>
    </Router>
  )
}

export default App;
