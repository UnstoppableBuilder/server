import { useEffect, useState } from 'react';
import { useParams } from "react-router-dom";

import '../pages/Page.css';

export default function ProjectList() {
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
          <a href=""></a>
        </div>
      </div>
    </div>
  </div>;
};
