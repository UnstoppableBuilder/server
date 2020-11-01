import { YMaps, Map, Polygon } from "react-yandex-maps";
import {useParams} from "react-router-dom";
import {useEffect, useState} from "react";


export default function ProjectWorkers(props) {
  const [zones, setZones] = useState({
    coords: [],
    center: [55.73, 37.9]
  })
  useEffect(() => {
    fetch(`/api/workplace/${props.item.id}/zones/`).then((result) => {
      return result.json()
    }).then((data) => {
      console.log(data);
      setZones(data);
    })
  }, [props.item.id]);

  return <YMaps>
    <Map
      defaultState={{
        center: zones.center,
        zoom: 17,
      }}
      width={"100%"}
      height={500}
    >
      <Polygon
        geometry={zones.coords}
        options={{
          fillColor: '#00FF00',
          strokeColor: '#0000FF',
          opacity: 0.3,
          strokeWidth: 3,
          strokeStyle: 'solid',
        }}
      />
    </Map>
  </YMaps>;
};
