import React from "react";
import NavMenu from "../../components/NavMenu";

import img from "../../images/pic1.png";

import "./index.scss";

const tabs = [
  { href: "/signIn", name: "Sign In" },
  { href: "/signUp", name: "Sign Up" },
];

const LandingPage = () => {
  return (
    <div className="landingPage">
      <NavMenu tabs={tabs} />
      <div className="landPageBody">
        <div className="landPageBodyItem left">
          <div>WELCOME TO 9I HOLDINGS</div>
          <div>NO CODE CHATBOT BUILDER</div>
        </div>
        {/* <div className="landPageBodyItem right">
          <img src={img} alt="landing page" />
        </div> */}
      </div>
    </div>
  );
};

export default LandingPage;
