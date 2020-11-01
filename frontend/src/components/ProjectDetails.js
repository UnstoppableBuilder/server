import { useEffect, useState } from 'react';
import {
  Switch,
  Route,
  NavLink,
  useRouteMatch,
  useParams
} from "react-router-dom";

import { ReactComponent as SvodkaIcon } from '../icons/svodka.svg';
import { ReactComponent as HeadIcon } from '../icons/littlehead.svg';
import { ReactComponent as ChatIcon } from '../icons/chat.svg';
import { ReactComponent as CalendarIcon } from '../icons/calendar.svg';
import { ReactComponent as ProjectIcon } from '../icons/projects.svg';

import '../pages/Page.css';
import ProjectWorkers from "./ProjectWorkers";


export default function ProjectDetails() {
  const match = useRouteMatch();
  const { projectId } = useParams();
  const [item, setItem] = useState(null)
  useEffect(() => {
    fetch(`/api/workplace/${projectId}/`).then((result) => {
      return result.json()
    }).then((data) => {
      setItem(data);
    })
  }, []);

  if (!item) {
    return <h3>Загрузка...</h3>
  }

  return <div className="page">
    <div className="page-header">
      <div className="title">
        <h1>{item.name}</h1>
        <p>Проекты</p>
      </div>
      {/*<div className="search"></div>*/}
      {/*<div className="button"></div>*/}
      {/*<div className="login"></div>*/}
    </div>
    <div className="page-white">
      <div className="sub-nav">
        <div className="sub-nav-item">
          <NavLink to={`${match.url}`} exact={true}><SvodkaIcon />&nbsp;Статистика</NavLink>
        </div>
        <div className="sub-nav-item">
          <NavLink to={`${match.url}/workers`}><HeadIcon />&nbsp;Сотрудники</NavLink>
        </div>
        <div className="sub-nav-item">
          <NavLink to={`${match.url}/chat`}><ChatIcon />&nbsp;Чат</NavLink>
        </div>
        <div className="sub-nav-item">
          <NavLink to={`${match.url}/calendar`}><CalendarIcon />&nbsp;Календарный план</NavLink>
        </div>
        <div className="sub-nav-item">
          <NavLink to={`${match.url}/info`}><ProjectIcon />&nbsp;Паспорт проекта</NavLink>
        </div>
      </div>
      <Switch>
        <Route path={`${match.path}/workers`}>
          <ProjectWorkers item={item} projectId={projectId} />
        </Route>
        <Route path={match.path}>
          <ProjectWorkers item={item} projectId={projectId} />
        </Route>
      </Switch>
    </div>
  </div>;
};
