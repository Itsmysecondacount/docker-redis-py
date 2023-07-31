import React from "react";
import { Form } from "./Form";
import { TimbreList } from "./Timbre";
import { Timbre } from './Interface';

const App: React.FC = () => {
  const [timbres, setTimbres] = React.useState<Timbre[]>([]);

  React.useEffect(() => {
    // sustituye 'http://localhost:8000/api/timbre' con la URL de tu API
    fetch('http://my-python-app:8000/api/timbre')
      .then((response) => response.json())
      .then(setTimbres);
  }, []);

  const addTimbre = (timbre: Timbre) => {
    // sustituye 'http://localhost:8000/api/timbre' con la URL de tu API
    fetch('http://my-python-app:8000/api/timbre', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(timbre),
    })
      .then((response) => response.json())
      .then((newTimbre) => {
        setTimbres((prevTimbres) => [...prevTimbres, newTimbre]);
      });
  };

  return (
    <div>
      <h1>Timbres</h1>
      <TimbreList timbres={timbres} />
      <Form onAdd={addTimbre} />
    </div>
  );
};

export default App;
