import { Present } from "../Objects/Present";
import { useState } from "react";

var localhost = 'http://127.0.0.1:5000/presents/Get'

export function Get(){
  document.body.style.backgroundColor = "red";
  const[divText] = useState('');
  const a = <div id="idf">
              {divText}
            </div>
  fetch(localhost)
    .then(response => response.json()).then(data => 
      {
        var par = document.getElementById("idf");
        data.forEach(addData)
        function addData(item) 
        {
          par.innerText += item.id;
          par.innerText += item.name;
          par.innerText += item.owner;
        };
      }
    );

 
  return (a);
}



//get

//getbyid

//add

//remove

//update