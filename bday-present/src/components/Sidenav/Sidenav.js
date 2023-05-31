import { NavLink } from "react-router-dom";
import { navData } from "./NavData";
import React, { useState } from 'react';

import "./Sidenav.css";

function Sidenav(){
    const [open, setopen] = useState(true);

    const toggleOpen = () => setopen(!open);

    return (  
        <div className= {open?"sidenav":"sidenaveClosed"}>
            <button className="menuBtn" onClick={toggleOpen}>
                Click me
            </button>
                {navData.map(item =>{
                    return <NavLink key={item.id} className="sideitem" to={item.link}>
                {item.icon}
                <span className="linkText">{item.text}</span>
            </NavLink>
            })}
        </div>
    );
}

export default Sidenav;