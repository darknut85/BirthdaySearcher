import { Home } from "../Home/Home";
import { ViewPresents } from "../Presents/Presents";

function App() {
  let home = false;
  if(home)
    return Home();
  else
    return ViewPresents();
}
export default App;
