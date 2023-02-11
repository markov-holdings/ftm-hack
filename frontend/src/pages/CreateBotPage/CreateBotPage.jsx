
import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import {Box} from '@mui/material';
import HistoryEduIcon from '@mui/icons-material/HistoryEdu';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
// import TableRows from "./TableRows"
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import MultipleValueTextInput from 'react-multivalue-text-input';

import { useState, useEffect } from 'react';
import Popup from './Popup';

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © 9i Holdings '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

// function AddDeleteTableRows(){
//     const [rowsData, setRowsData] = useState([]);
 
//     const addTableRows = ()=>{
  
//         const rowsInput={
//             Intent:'',
//             Utterances:'',
//             Prompts:''  
//         } 
//         setRowsData([...rowsData, rowsInput])
      
//     }
//    const deleteTableRows = (index)=>{
//         const rows = [...rowsData];
//         rows.splice(index, 1);
//         setRowsData(rows);
//    }
 
//    const handleChange = (index, evnt)=>{
    
//     const { name, value } = evnt.target;
//     const rowsInput = [...rowsData];
//     rowsInput[index][name] = value;
//     setRowsData(rowsInput);
// }
// }



const theme = createTheme();


export default function CreateBotPage() {

  const URL = 'http://127.0.0.1:8000/api/chatbot/'

  const postData = async (event) => {
    const response = await fetch(URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"name": name,
                            "social_media_type": "instagram",
                            "description":description,
                            "chatbot_intents": [
                              {
                                  "name": firstIntent,
                                  "utterances": [{"content":firstUtteranceFirstIntent}, {"content":secondUtteranceFirstIntent}],
                                  "slots": [{"content":firstResponse}],
                              },
                              {
                                  "name": secondIntent,
                                  "utterances": [{"content":firstUtteranceSecondIntent}, {"content":secondUtteranceSecondIntent}],
                                  "slots": [{"content":secondResponse}],
                              }
                            ]})
    });

    const data = await response.json
    if (response.ok) {
            console.log(data)
        } else {
            console.log('Failed Network Request')
        }
    return response.json();
  }
  
  // const handleSubmit = async (event) => {
  //   event.preventDefault();
  //   const new_request = new Request(
  //     `http://127.0.0.1:8000/api/chatbot/`, 
  //     {
  //         body: JSON.stringify({firstIntent, 
  //                               secondIntent,
  //                               firstUtteranceFirstIntent,
  //                               secondUtteranceFirstIntent,
  //                               firstResponse,
  //                               firstUtteranceSecondIntent,
  //                               secondUtteranceSecondIntent,
  //                               secondResponse}),
  //         headers:{
  //             'Content-Type':'Application/Json'
  //         },
  //         method: 'POST'
  //     }
  //   );

  //   const response = await fetch(new_request);

  //   const data = await response.json()

  //   if (response.ok) {
  //       console.log(data)
  //   } else {
  //       console.log('Failed Network Request')
  //   }
  // };
  


  const [isOpen, setIsOpen] = useState(false);

  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const [firstIntent, setFirstIntent] = useState('');
  const [secondIntent, setSecondIntent] = useState('');
  const [firstUtteranceFirstIntent, setFirstUtteranceFirstIntent] = useState('');
  const [secondUtteranceFirstIntent, setSecondUtteranceFirstIntent] = useState('');

  const [firstResponse, setFirstResponse] = useState('');
  const [firstUtteranceSecondIntent, setFirstUtteranceSecondIntent] = useState('');
  const [secondUtteranceSecondIntent, setSecondUtteranceSecondIntent] = useState('');
  const [secondResponse, setSecondResponse] = useState('');


  

 
  const togglePopup = () => {
    setIsOpen(!isOpen);
  }

  return (
    <ThemeProvider theme={theme}>
      <div style = {{paddingTop: "100px"}}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 2,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <HistoryEduIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Form Submission
          </Typography>
          {/* <div className="container">
            <div className="row">
                <div className="col-sm-8">
                <table className="table">
                    <thead>
                      <tr>
                          <th>Full Name</th>
                          <th>Email Address</th>
                          <th>Salary</th>
                          <th><button className="btn btn-outline-success" onClick={addTableRows} >+</button></th>
                      </tr>
                    </thead>
                   <tbody>
                   <TableRows rowsData={rowsData} deleteTableRows={deleteTableRows} handleChange={handleChange} />
                   </tbody> 
                </table>
                </div>
                <div className="col-sm-4">
                </div>
            </div>
        </div> */}
          
          <Box component="form" noValidate onSubmit={postData} sx={{ mt: 12 }}>
          <Grid container spacing={2}>
            <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="name"
                  label="Name"
                  name="name"
                  autoComplete="name"
                  onChange = {(e) => setName(e.target.value)}
                />
              </Grid>
            <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="description"
                  label="Description"
                  name="description"
                  autoComplete="description"
                  onChange = {(e) => setDescription(e.target.value)}
                  />
                </Grid>
              <Grid item xs={12}>
                {/* <p>Gender: </p> */}
                <input type="radio" value="facebook" name="social media" /> Facebook  
                <input type="radio" value="instagram" name="social media" /> Instagram  
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="intent"
                  label="Action 1"
                  name="intent1"
                  autoComplete="intent1"
                  onChange = {(e) => setFirstIntent(e.target.value)}
                />
              </Grid>
              <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
              </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Sample Trigger"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setFirstUtteranceFirstIntent(e.target.value)}
                />
              </Grid>
              <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
              </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Sample Trigger"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setSecondUtteranceFirstIntent(e.target.value)}
                />
              
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Response 1"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setFirstResponse(e.target.value)}
                />
              </Grid>
                <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Name"
                  name="utterance 1"
                  autoComplete="utterance 1"
                />
              </Grid>
              <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Response Message"
                  name="utterance 1"
                  autoComplete="utterance 1"
                />
              </Grid>
              <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs = {11}>
              <MultipleValueTextInput
                style = {{height: '60px', width: '366px', borderRadius: '5px', borderWidth: 'thin', fontSize: '15px'}}
                onItemAdded={(item, allItems) => console.log(`Item added: ${item}`)}
                onItemDeleted={(item, allItems) => console.log(`Item removed: ${item}`)}
                name="item-input"
                placeholder="Response choices"
                className = 'multiple-select'
                deleteButton={<span>x</span>}

              />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Response 2"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setFirstResponse(e.target.value)}
                />
              </Grid>
                <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Name"
                  name="utterance 1"
                  autoComplete="utterance 1"
                />
              </Grid>
              <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Response Message"
                  name="utterance 1"
                  autoComplete="utterance 1"
                />
              </Grid>
              <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs = {11}>
              <MultipleValueTextInput
                style = {{height: '60px', width: '366px', borderRadius: '5px', borderWidth: 'thin', fontSize: '15px'}}
                onItemAdded={(item, allItems) => console.log(`Item added: ${item}`)}
                onItemDeleted={(item, allItems) => console.log(`Item removed: ${item}`)}
                name="item-input"
                placeholder="Response choices"
                className = 'multiple-select'
                deleteButton={<span>x</span>}

              />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Response 3"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setFirstResponse(e.target.value)}
                />
              </Grid>
                <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Name"
                  name="utterance 1"
                  autoComplete="utterance 1"
                />
              </Grid>
              <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Response Message"
                  name="utterance 1"
                  autoComplete="utterance 1"
                />
              </Grid>
              <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs = {11}>
              <MultipleValueTextInput
                style = {{height: '60px', width: '366px', borderRadius: '5px', borderWidth: 'thin', fontSize: '15px'}}
                onItemAdded={(item, allItems) => console.log(`Item added: ${item}`)}
                onItemDeleted={(item, allItems) => console.log(`Item removed: ${item}`)}
                name="item-input"
                placeholder="Response choices"
                className = 'multiple-select'
                deleteButton={<span>x</span>}

              />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Confirmation"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setFirstResponse(e.target.value)}
                />
              </Grid>
                <Grid item xs={1}>
                <TextField
                  disabled
                  id="outlined-disabled"
                  label=""
                />
                </Grid>
              <Grid item xs={11}>
                <TextField
                  required
                  fullWidth
                  id="utterance"
                  label="Confirmation message"
                  name="utterance 1"
                  autoComplete="utterance 1"
                />
              </Grid>
              
              {/* <Grid item xs={12}>
                <LocalizationProvider dateAdapter={AdapterDayjs}>
                  <DatePicker
                    label="Basic example"
                    value={value}
                    onChange={(newValue) => {
                      setValue(newValue);
                    }}
                    renderInput={(params) => <TextField {...params} />}
                  />
                </LocalizationProvider>
              </Grid> */}
              
              
            </Grid>
            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%', paddingTop: '10px'}}>
            <button style ={{backgroundColor: 'black', color: 'white', borderRadius: '10px', padding: '10px 20px', fontSize: '15px'}}>Add more Actions</button>
          </div>
            <div style={{ display: 'flex', justifyContent: 'right', alignItems: 'right', paddingTop: '20px'}}>
              <input
              style ={{backgroundColor: 'black', color: 'white', borderRadius: '10px', padding: '10px 20px', fontSize: '20px'}}
                type="submit"
                fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
                value="Submit"
                onClick={togglePopup}
              />
              {/* <p>Submit</p> */}
              {isOpen && <Popup
              //   content={<>
              //     <b>Bot is being created</b>
              //     <p>Intent and Utterances has been successfully sent to the database.</p>
              //     <Grid item>
              //   <Link href="../user/videos" variant="body2">
              //     {"Acknowledged"}
              //   </Link>
              // </Grid>
              //   </>}
              //   handleClose={togglePopup}
               />}
            </div>
            {/* <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              onClick = {togglePopup}
            >
              Create Bot
              {isOpen && <Popup
      content={<>
        <b>Bot is being created</b>
        <button>Understood</button>
      </>}
      handleClose={togglePopup}
    />}
            </Button> */}
          </Box>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
      </div>
    </ThemeProvider>
  );
}