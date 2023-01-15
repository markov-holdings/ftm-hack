import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import "./index.scss";

const videos = [
  {
    type: "instagram",
    src: "https://www.youtube.com/embed/nJAomDq_ZUk",
  },
  {
    type: "facebook",
    src: "https://www.youtube.com/embed/2_aFCSXMA2o",
  },
];

const VideoPage = () => {
  const [search, setSearch] = useState("");
  const filteredVideos = videos.filter(
    (video) =>
      Boolean(search) && video.type.toLowerCase().indexOf(search) !== -1
  );

  return (
    <div className="videoPage">
      <div className="videoPageTitle">Videos</div>
      <TextField
        id="outlined-basic"
        label="Topic"
        variant="outlined"
        onChange={(e) => setSearch(e.target.value)}
      />
      <div className="videoContainer">
        {filteredVideos.length === 0 ? (
          <div className="videoNotSearch">No videos searched yet</div>
        ) : (
          filteredVideos.map((video) => (
            <iframe
              width="560"
              height="315"
              src={video.src}
              title="YouTube video player"
              frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            />
          ))
        )}
      </div>
    </div>
  );
};

export default VideoPage;
