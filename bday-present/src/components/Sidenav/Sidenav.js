import { navData } from "./NavData";
import "./Sidenav.css";

export default function Sidenav(){
    return (  
        <div>
            <button className="menuBtn">
                Click me
            </button>
                {navData.map(item =>{
                    return <div key={item.id} className="sideitem">
            {item.icon}
            <span className="linkText">{item.text}</span>
            </div>
            })}
        </div>
    );
}