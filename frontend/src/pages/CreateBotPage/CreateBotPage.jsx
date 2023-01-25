
import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import HistoryEduIcon from '@mui/icons-material/HistoryEdu';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
// import TableRows from "./TableRows"
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

import { useState } from 'react';
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
  
  const handleSubmit = async (event) => {
    event.preventDefault();
    const new_request = new Request(
      `http://127.0.0.1:8000/api/chatbot/`, 
      {
          body: JSON.stringify({firstIntent, 
                                secondIntent,
                                firstUtteranceFirstIntent,
                                secondUtteranceFirstIntent,
                                firstResponse,
                                firstUtteranceSecondIntent,
                                secondUtteranceSecondIntent,
                                secondResponse}),
          headers:{
              'Content-Type':'Application/Json'
          },
          method: 'POST'
      }
    );

    const response = await fetch(new_request);

    const data = await response.json()

    if (response.ok) {
        console.log(data)
    } else {
        console.log('Failed Network Request')
    }
  };
  const [isOpen, setIsOpen] = useState(false);
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
            marginTop: 8,
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
          
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
          <Grid container spacing={2}>

              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="intent"
                  label="First Intent"
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
                  label="First Utterance for intent 1"
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
                  label="Second Utterance for intent 1"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setSecondUtteranceFirstIntent(e.target.value)}
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
                  label="Response"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setFirstResponse(e.target.value)}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id="intent"
                  label="Second Intent"
                  name="intent2"
                  autoComplete="intent2"
                  onChange = {(e) => setSecondIntent(e.target.value)}
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
                  label="First Utterance for intent 2"
                  name="utterance 1"
                  autoComplete="utterance 1"
                  onChange = {(e) => setFirstUtteranceSecondIntent(e.target.value)}
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
                  label="Second Utterance for intent 2"
                  name="utterance 2"
                  autoComplete="utterance 1"
                  onChange = {(e) => setSecondUtteranceSecondIntent(e.target.value)}
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
                  label="Response"
                  name="utterance 2"
                  autoComplete="utterance 1"
                  onChange = {(e) => setSecondResponse(e.target.value)}
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
            <div>
              <input
                type="submit"
                fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
                value="Submit"
                onClick={togglePopup}
              />
              {/* <p>Submit</p> */}
              {isOpen && <Popup
                content={<>
                  <b>Bot is being created</b>
                  <p>Intent and Utterances has been successfully sent to the database.</p>
                  <Grid item>
                <Link href="../user/videos" variant="body2">
                  {"Acknowledged"}
                </Link>
              </Grid>
                </>}
                handleClose={togglePopup}
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