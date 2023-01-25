import React from "react";
import { Outlet, useLocation } from "react-router-dom";
import NavMenu from "../../components/NavMenu";
import clothing from "../../images/bot-clothing.jpg";
import flower from "../../images/bot-flower.jpg";

import "./index.scss";

const tabs = [
  { href: "/user", name: "Home" },
  { href: "/user/videos", name: "Video" },
  { href: "/user/managebot", name: "Manage Bot"},
  { href: "/user/createBot", name: "Bot Creation" },

];

const botServices = [
  {
    img: flower,
    text: "Bot for selling flowers",
  },
  {
    img: clothing,
    text: "Bot for selling clothings",
  },
];

const ManageBotPage = () => {
  const location = useLocation();

  return (
    <>
      <NavMenu tabs={tabs} />
      {location.pathname === "/user/managebot" ? (
        <div className="manageBotPage">
          <div className="manageBotPageTitle">Click cards to know mroe or edit the bots</div>
          <div className="manageBotPageCards">
            {botServices.map((service) => (
              <div className="manageBotPageCard">
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

export default ManageBotPage;
