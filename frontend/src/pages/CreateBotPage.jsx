
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
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      name: data.get('name'),
      password: data.get('password'),
    });
  };

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
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Create Bot
            </Button>
          </Box>
        </Box>
        <Copyright sx={{ mt: 5 }} />
      </Container>
      </div>
    </ThemeProvider>
  );
}