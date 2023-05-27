var localhost = 'http://127.0.0.1:5000/presents/Get'

export function changeText(){
    fetch(localhost)
    .then(response => response.json()).then(data => 
      {
        console.log(data);
      }
    );
  }



//get

//getbyid

//add

//remove

//update