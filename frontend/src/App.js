// import drfProvider from 'ra-data-drf';
//
// import { Admin, Resource } from 'react-admin';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  NavLink
} from "react-router-dom";

import { ReactComponent as Logo } from './logo.svg';
import { ReactComponent as Footer } from './icons/footer.svg';

import { ReactComponent as EmployersIcon } from './icons/employers.svg';
import { ReactComponent as NotificationsIcon } from './icons/notifications.svg';
import { ReactComponent as ProjectsIcon } from './icons/projects.svg';
import { ReactComponent as SettingsIcon } from './icons/settings.svg';
import { ReactComponent as SosIcon } from './icons/sos.svg';
import { ReactComponent as SvodkaIcon } from './icons/svodka.svg';
import { ReactComponent as WorkersIcon } from './icons/workers.svg';

import Employers from "./pages/Employers";
import Notifications from "./pages/Notifications";
import Projects from "./pages/Projects";
import Settings from "./pages/Settings";
import Sos from "./pages/Sos";
import Svodka from "./pages/Svodka";
import Workers from "./pages/Workers";

import './App.css';


function App() {
  return (
    <Router>
      <div className="container">
        <div className="menu">
          <div className="menuUp">
            <Logo className="logo" />
            <div className="nav">
              <NavLink activeClassName="active" exact={true} to="/"><SvodkaIcon /> Сводка</NavLink>
              <NavLink activeClassName="active" to="/projects"><ProjectsIcon /> Проекты</NavLink>
              <NavLink activeClassName="active" to="/workers"><WorkersIcon /> Сотрудники</NavLink>
              <NavLink activeClassName="active" to="/employers"><EmployersIcon /> Работодатели</NavLink>
              <NavLink activeClassName="active" to="/notifications"><NotificationsIcon /> Уведомления</NavLink>
              <NavLink activeClassName="active" to="/sos"><SosIcon /> SOS</NavLink>
              <NavLink activeClassName="active" to="/settings"><SettingsIcon /> Настройки</NavLink>
            </div>
          </div>
          <div className="menuDown">
            <Footer/>
          </div>
        </div>
        <div className="content">
          <Switch>
            <Route exact path="/"><Svodka /></Route>
            <Route path="/projects"><Projects /></Route>
            <Route path="/workers"><Workers /></Route>
            <Route path="/employers"><Employers /></Route>
            <Route path="/notifications"><Notifications /></Route>
            <Route path="/sos"><Sos /></Route>
            <Route path="/settings"><Settings /></Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
