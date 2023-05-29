import { Present } from "../Objects/Present";
import React, { useEffect, useState } from 'react';

const restEndpoint = "http://127.0.0.1:5000/presents/Get";



export function Get() {
  const callRestApi = async () => {
    const response = await fetch(restEndpoint);
    const jsonResponse = await response.json();

    const js = JSON.stringify(jsonResponse);
    const parsed = JSON.parse(js);
    console.log(parsed);

    return React.createElement('div', null, js);
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

//foreach the html
//count is added to the id of the html
//use unique id in get method



//get

//getbyid

//add

//remove

//update