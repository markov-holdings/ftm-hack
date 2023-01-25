import React from "react";
import { Outlet, useLocation } from "react-router-dom";
import NavMenu from "../../components/NavMenu";
import user1pic from "../../images/user1pic.png";
import user2pic from "../../images/user2pic.png";
import user3pic from "../../images/user3pic.png";

import "./index.scss";

const tabs = [
  { href: "/user", name: "Home" },
  { href: "/user/videos", name: "Video" },
  { href: "/user/managebot", name: "Manage Bot"},
  { href: "/user/createBot", name: "Bot Creation" },

];

const supportServices = [
  {
    img: user1pic,
    text: "FaceBook messenger",
  },
  {
    img: user2pic,
    text: "Instagram messenger",
  },
  {
    img: user3pic,
    text: "Web messenger",
  },
];

const LoggedInPage = () => {
  const location = useLocation();

  return (
    <>
      <NavMenu tabs={tabs} />
      {location.pathname === "/user" ? (
        <div className="loggedInPage">
          <div className="loggedInPageTitle">Learn more about</div>
          <div className="loggedInPageCards">
            {supportServices.map((service) => (
              <div className="loggedInPageCard">
                <img src={service.img} alt={service.text} />
                <div>{service.text}</div>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <Outlet />
      )}
    </>
  );
};

export default LoggedInPage;
