import {
  Switch,
  Route,
  useRouteMatch,
} from "react-router-dom";

import ProjectList from "../components/ProjectList";
import ProjectDetails from "../components/ProjectDetails";

import './Page.css';

export default function Projects() {
  let match = useRouteMatch();
  return <Switch>
        <Route path={`${match.path}/:projectId`}>
          <ProjectDetails />
        </Route>
        <Route path={match.path}>
          <ProjectList />
        </Route>
      </Switch>;
};
