import React, { useEffect, useState } from 'react';

const restEndpoint = "http://127.0.0.1:5000/presents/Get";

//get
export function Get() {
  const callRestApi = async () => {
    const response = await fetch(restEndpoint);
    const jsonResponse = await response.json();

    const js = JSON.stringify(jsonResponse);
    const parsed = JSON.parse(js);
    const pList = []
    const presents = <div>{pList}</div>

    parsed.forEach(element => {
      pList.push(<div>dd: {element.id}, name: {element.name}, owner: {element.owner}</div>);
    });
    return presents;
  };

  const [apiResponse, setApiResponse] = useState("*** now loading ***");

  useEffect(() => {
    callRestApi().then(
      result => setApiResponse(result));
  },[]);
  
  return (<div>
            {apiResponse}
         </div>
  );
};

//getbyid

//add

//remove

//update