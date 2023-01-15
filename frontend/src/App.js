import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import LoggedInPage from "./pages/LoggedInPage/LoggedInPage";
import SignInPage from "./pages/SignInPage";
import SignUpPage from "./pages/SignUpPage";
import LandingPage from "./pages/LandingPage";
import CreateBotPage from "./pages/CreateBotPage";
import VideoPage from "./pages/VideoPage";


// Add redirect upon not log in.
function App() {
  return (
    <Router>
      <Routes>
        <Route path="user" element={<LoggedInPage />}>
          <Route path="videos" element={<VideoPage />} />
          <Route path="createBot" element={<CreateBotPage />} />
        </Route>
        <Route path="signIn" element={<SignInPage />} />
        <Route path="signUp" element={<SignUpPage />} />
        <Route path="/" element={<LandingPage />} />
      </Routes>
    </Router>
  );
}

export default App;
