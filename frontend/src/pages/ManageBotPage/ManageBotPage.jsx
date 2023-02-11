import React, { useState, useEffect } from "react";
import TextField from "@mui/material/TextField";
import "./index.scss";
import { Button } from "react-bootstrap";



const ManageBotPage = () => {
  const initialState = "Build Bot";
  const endState = "Bot has been built";
  const [buttonText, setButtonText] = useState("Build Bot");
  const [name, setName] = useState('name');

  useEffect(() => { 
    if(buttonText === 'Building Bot'){
      setTimeout(() => setButtonText(endState), [5000])
    }
  }, [buttonText])

  const changeText = (text) => setButtonText(text);

  return (
    <div className="App">
      <table>
        <tr>
          <th>No.</th>
          <th>Name</th>
          <th>Edit</th>
          <th>Delete</th>
          <th>Deploy</th>
          {/* <th>Status</th> */}
        </tr>
        

            <tr>
              <td>1</td>
              <td>Gardening Tools shop</td>
              <td><Button> Edit </Button></td>
              <td><Button color="red" appearance="primary"> Delete </Button></td>
              <td><Button >Build Bot</Button></td>

            </tr>
            <tr>
              <td>2</td>
              <td>Flower shop</td>
              <td><Button> Edit </Button></td>
              <td><Button color="red" appearance="primary"> Delete </Button></td>
              <td><button type="button" onClick={() => changeText("Building Bot")}>{buttonText}</button></td>
            </tr>
          
        
      </table>
    </div>
  );
};

export default ManageBotPage;


