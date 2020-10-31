import {ReactComponent as BoxIcon} from "../icons/box.svg";
import {ReactComponent as KranIcon} from "../icons/kran.svg";
import {ReactComponent as HeadIcon} from "../icons/head.svg";

import './ProjectItem.css';

export default function ProjectItem(props) {
  return <a href="#" className="project-item">
    <div className="title">
      <h3>{props.item.name}</h3>
      <p>{props.item.contract}</p>
    </div>
    <div className="info">
      <div className="list">
        <p><BoxIcon />&nbsp;&nbsp;{props.item.customer}</p>
        <p><KranIcon />&nbsp;&nbsp;{props.item.contractor}</p>
      </div>
    </div>
    <div className="count">
      {props.item.worker_count}&nbsp;<HeadIcon />
    </div>
  </a>;
}
