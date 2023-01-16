import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useWindowSize } from "../../hooks/useWindowSize";
import img from "../../images/logo.png";

import "./index.scss";

const NavMenu = ({ tabs }) => {
  const { width } = useWindowSize();
  const navigate = useNavigate();
  const [click, setClick] = useState(false);

  // this is to prevent multiple event listeners.
  useEffect(() => {
    setValuesBasedOnWidth();
    window.addEventListener("resize", setValuesBasedOnWidth);

    return () => {
      window.removeEventListener("resize", setValuesBasedOnWidth);
    };
  }, []);

  const toggleClick = () => setClick(!click);

  const handleClick = (href) => {
    if (href) {
      setClick(false);
      navigate(href);
      return;
    }

    // all other cases
    toggleClick();
  };

  const setValuesBasedOnWidth = () => {
    if (window.innerWidth >= 860) {
      setClick(false);
    }
  };

  if (width == null) return null;

  if (width < 860) {
    return (
      <>
        <nav className="nav">
          <div className="navContainer">
            <img
              className="title"
              onClick={() => handleClick("/")}
              src = {img}
              alt="logo"
            />
            <div className="hamburger" onClick={() => handleClick()}>
              <div className={`bar ${!click ? "" : "active"}`} />
            </div>
          </div>
        </nav>
        <div className={`dropdown-list ${!click ? "inactive" : "active"}`}>
          {tabs.map((tab) => (
            <p
              className="vertical-tab"
              onClick={() => handleClick(tab.href)}
              key={tab}
            >
              {tab.name}
            </p>
          ))}
        </div>
      </>
    );
  }

  return (
    <nav className="nav">
      <div className="navContainer">
        <img
          className="title"
          onClick={() => handleClick("/")}
          src={img}
          alt="logo"
        />
        <div className="horizontal-tabs">
          {tabs.map((tab) => (
            <p className="horizontal-tab" onClick={() => handleClick(tab.href)}>
              {tab.name}
            </p>
          ))}
        </div>
      </div>
    </nav>
  );
};

export default NavMenu;
