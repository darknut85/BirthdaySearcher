import { NavLink } from "react-router-dom";
import { navData } from "./NavData";
import React, { useState } from 'react';

import "./Sidenav.css";

function Sidenav(){
    const [open, setopen] = useState(true);

    const toggleOpen = () => setopen(!open);

    return (  
        <div className= {open?"sidenav":"sidenavClosed"}>
            <button className="menuBtn" onClick={toggleOpen}>
                Toggle sidenav
            </button>
                {navData.map(item =>{
                    return <NavLink key={item.id} className="sideitem" to={item.link}>
                {item.icon}
                <span className={open?"linkText":"linkTextClosed"}>{item.text}</span>
            </NavLink>
            })}
        </div>
    );
}

export default Sidenav;