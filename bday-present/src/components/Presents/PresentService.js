import { Present } from "../Objects/Present";
import { useState } from "react";

var localhost = 'http://127.0.0.1:5000/presents/Get'

export function Get(){
  document.body.style.backgroundColor = "red";
  const[divText] = useState('');

  fetch(localhost)
    .then(response => response.json()).then(data => 
      {
        var idf = document.getElementById("idf");
        var idn = document.getElementById("idn");
        var ido = document.getElementById("ido");

        data.forEach(addData)
        function addData(item) 
        {
          const present = new Present(item.id,item.name,item.owner);
          idf.innerText += present.id + "\n";
          idn.innerText += present.name + "\n";
          ido.innerText += present.owner + "\n";
        };
      }
    );
  const a = 
  <div>
    <div id="idf">
      {divText}
    </div>
    <div id="idn">
      {divText}
    </div>
    <div id="ido">
      {divText}
    </div>
  </div>
    
  return (a);
}



//get

//getbyid

//add

//remove

//update