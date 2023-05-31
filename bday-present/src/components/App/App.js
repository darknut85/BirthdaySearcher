import { Routes, Route } from "react-router-dom";
import Home from "../Home/Home";
import { ViewPresents } from "../Presents/Presents";
import Sidenav from "../Sidenav/Sidenav";
import './App.css';

function App() {
  return (
    <div className="App">
      <Sidenav/>
      <main>
        <Routes>
          <Route path="/" element={<Home />}/>
          <Route path="/Get" element={<ViewPresents />} />
        </Routes>
      </main>
    </div>
  );
}
export default App;






/**
function appp(){

  let home = 2;
  if(home == 0)
    return Home();
  else if (home == 1)
    return ViewPresents();
}
 */

