import { ReactComponent as Arrow } from '../icons/arrow.svg';

import { useEffect, useState } from 'react';
import ProjectItem from './ProjectItem';

import '../pages/Page.css';

export default function ProjectList() {
  const [list, setList] = useState([])
  useEffect(() => {
    fetch("/api/workplace/").then((result) => {
      return result.json()
    }).then((data) => {
      setList(data);
    })
  }, []);

  const items = list.map((value, index) => {
    return <ProjectItem item={value} key={index} />
  });

  return <div className="page">
    <div className="page-header">
      <div className="title">
        <h1>Проекты</h1>
        <p>Сначала более новые&nbsp;<Arrow /></p>
      </div>
      <div className="search"></div>
      <div className="button"></div>
      <div className="login"></div>
    </div>
    <div className="page-content">
      {items}
    </div>
  </div>;
};
