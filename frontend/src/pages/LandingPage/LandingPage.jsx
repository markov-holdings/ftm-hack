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
          <div>Welcome to 9i Holdings</div>
          <div>DO WHAT INSPIRES</div>
          <div>
            Automate everything else
          </div>
        </div>
        <div className="landPageBodyItem right">
          <img src={img} alt="landing page" />
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
