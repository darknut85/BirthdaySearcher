import { Present } from "../Objects/Present";
import { useState } from "react";

var localhost = 'http://127.0.0.1:5000/presents/Get'

export function Get(){
  document.body.style.backgroundColor = "red";
  const[divText] = useState('');

  fetch(localhost)
    .then(response => response.json()).then(data => 
      {
        var par = document.getElementById("idf");

        data.forEach(addData)
        function addData(item) 
        {
          const present = new Present(item.id,item.name,item.owner);
          par.innerText += present.id;
          par.innerText += present.name;
          par.innerText += present.owner;
        };
      }
    );
  const a = <div id="idf">
              {divText}
            </div>
    
  return (a);
}



//get

//getbyid

//add

//remove

//update